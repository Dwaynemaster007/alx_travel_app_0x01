# ✈️ ALX Travel App 0x01: REST API

Milestone 0x01 of the travel booking API: CRUD endpoints for listings and bookings, built with Django REST Framework `ModelViewSet`s and a router.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)

## What's in this milestone

| File | Purpose |
| --- | --- |
| [`listings/views.py`](alx_travel_app/listings/views.py) | `ListingViewSet` and `BookingViewSet` |
| [`listings/urls.py`](alx_travel_app/listings/urls.py) | `DefaultRouter` that exposes `/api/listings/` and `/api/bookings/` |

| Method | Endpoint | Action |
| --- | --- | --- |
| `GET` `POST` | `/api/listings/` | List or create listings |
| `GET` `PUT` `PATCH` `DELETE` | `/api/listings/{id}/` | Manage one listing |
| `GET` `POST` | `/api/bookings/` | List or create bookings |
| `GET` `PUT` `PATCH` `DELETE` | `/api/bookings/{id}/` | Manage one booking |

## The travel app series

Each repository holds the code added in one milestone of the **ALX ProDev Backend** travel booking project:

| Repo | Milestone |
| --- | --- |
| [`alx_travel_app`](https://github.com/Dwaynemaster007/alx_travel_app) | Project setup: Django, DRF, Swagger, MySQL configuration |
| [`alx_travel_app_0x00`](https://github.com/Dwaynemaster007/alx_travel_app_0x00) | Models (`Listing`, `Booking`, `Review`), serializers and a seed command |
| [`alx_travel_app_0x01`](https://github.com/Dwaynemaster007/alx_travel_app_0x01) | CRUD API with DRF `ViewSet`s and routers |
| [`alx_travel_app_0x02`](https://github.com/Dwaynemaster007/alx_travel_app_0x02) | Chapa payment initiation and verification |
| [`alx_travel_app_0x03`](https://github.com/Dwaynemaster007/alx_travel_app_0x03) | Celery + RabbitMQ background email tasks |

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
