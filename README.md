# ✈️ ALX Travel App 0x01: REST API

Milestone 0x01 of the travel booking API: CRUD endpoints for listings and bookings, built with Django REST Framework `ModelViewSet`s and a router.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)

## What's in this milestone

| Method | Endpoint | Who |
| --- | --- | --- |
| `GET` | `/api/listings/`, `/api/listings/{id}/` | Anyone |
| `POST` | `/api/listings/` | Signed-in users (you become the host) |
| `PUT` `PATCH` `DELETE` | `/api/listings/{id}/` | The listing's host |
| `GET` `POST` | `/api/bookings/` | Signed-in users; you only see your own bookings (staff see all) |
| `GET` `PUT` `PATCH` `DELETE` | `/api/bookings/{id}/` | The guest who made it |
| `GET` `POST` | `/api/reviews/` | Anyone can read; signed-in users can post |

`total_price` is calculated from the nightly rate, and check-out must be after check-in. Try it all at `/swagger/`.

## Run it

You need Python 3.10+. MySQL is optional: leave `DB_NAME` empty in `.env` to use SQLite.

```bash
git clone https://github.com/Dwaynemaster007/alx_travel_app_0x01.git
cd alx_travel_app_0x01
cd alx_travel_app
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt   # mysqlclient needs the MySQL client headers; remove it if you only use SQLite
cp .env.example .env
python manage.py migrate
python manage.py seed           # sample data
python manage.py runserver       # http://localhost:8000/swagger/
python manage.py test listings  # run the tests
```

## The travel app series

Each repository holds the project as it was at the end of one milestone:

| Repo | Milestone |
| --- | --- |
| [`alx_travel_app`](https://github.com/Dwaynemaster007/alx_travel_app) | Project setup: Django, DRF, CORS, Swagger, MySQL/SQLite settings |
| [`alx_travel_app_0x00`](https://github.com/Dwaynemaster007/alx_travel_app_0x00) | Models (`Listing`, `Booking`, `Review`), serializers and a `seed` command |
| **`alx_travel_app_0x01`** | CRUD API with DRF `ViewSet`s and a router |
| [`alx_travel_app_0x02`](https://github.com/Dwaynemaster007/alx_travel_app_0x02) | Chapa payment initiation and verification |
| [`alx_travel_app_0x03`](https://github.com/Dwaynemaster007/alx_travel_app_0x03) | Celery + RabbitMQ booking confirmation emails |

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
