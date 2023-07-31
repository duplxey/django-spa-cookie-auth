# Django + React SPA (cross origin)

Cookie based authentication, frontend and backend separated, cross origin

## Getting Started

Run Django:

```sh
$ cd backend
$ python3 -m venv venv && source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```

Run React:

```sh
$ cd frontend
$ npm install
$ npm run dev
```

Test at [http://localhost:5173/](http://localhost:5173/).
