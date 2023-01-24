# deploy.now
deploy.now - backend

### Commands used:
```bash
poetry install
poetry add black --group dev
docker-compose run --rm deploy-now bash -c "django-admin startproject app ."
docker-compose build
docker-compose up
```

Then, the backend runs in http://localhost:8070

Format all the project in the beggining:
```bash
black .
```

Test command (out-of-the-box Django Test Framework):
```bash
docker-compose run --rm deploy-now bash -c "python manage.py test"
```

Lint command:
```bash
docker-compose run --rm deploy-now bash -c "flake8"
```

Create super user:
```bash
docker-compose run --rm deploy-now bash -c "python manage.py createsuperuser"
````
