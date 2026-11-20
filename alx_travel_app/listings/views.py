from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Booking, Listing, Review
from .serializers import BookingSerializer, ListingSerializer, ReviewSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Anyone can read; only the listing's host can change it."""

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.host == request.user


class ListingViewSet(viewsets.ModelViewSet):
    """Browse listings; signed-in users can create them and edit their own."""
    queryset = Listing.objects.select_related('host')
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    """Users see and manage their own bookings; staff see all of them."""
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):  # drf-yasg builds the schema without a user
            return Booking.objects.none()
        user = self.request.user
        queryset = Booking.objects.select_related('listing', 'user')
        return queryset if user.is_staff else queryset.filter(user=user)

    def perform_create(self, serializer):
        # Booking.save() works out total_price from the nightly rate
        booking = serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    """Anyone can read reviews; signed-in users can post and edit their own."""
    queryset = Review.objects.select_related('user', 'listing')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied('You can only edit your own reviews.')
        serializer.save()
