# Django + DRF + React SPA (same origin)

Cookie based authentication, Django REST Framework, frontend and backend separated (same origin)

## Getting Started

```sh
$ docker-compose up -d --build
$ docker-compose exec backend python manage.py makemigrations
$ docker-compose exec backend python manage.py migrate
$ docker-compose exec backend python manage.py createsuperuser
```

[http://localhost:81/](http://localhost:81/)
