### How to run this project?
___

Run this command under the root of project: <code>docker-compose up --build</code>

Test it out:  http://localhost:8000

### Make migrations: 

<code>docker-compose exec web python manage.py migrate --noinput</code>

### Connect to database: 

<code>docker-compose exec db psql --username=currency-exchange-rate --dbname=currency-exchange-rate</code>

### Create app: 

<code>docker-compose exec web python manage.py startapp app_name</code>

### Run tests: 

<code>docker-compose exec web python manage.py test</code>

Visit, https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ for details.
