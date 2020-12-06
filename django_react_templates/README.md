# Django + React SPA served up via Django templates

Cookie based authentication, frontend served with Django templates

## Getting started

Create and activate a virtual environment:

```sh
$ python3 -m venv venv && source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python manage.py migrate

(venv)$ cd frontend
(venv)$ npm install
(venv)$ npm run build

(venv)$ cd ..
(venv)$ python manage.py runserver
```

Test at [http://localhost:8000/](http://localhost:8000/).
