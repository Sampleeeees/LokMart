# Definition
MANAGE = python manage.py
SOURCE = src

# python base commands

run:
	$(MANAGE) create_superuser
	$(MANAGE) runserver

mm:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate


# docker command
start-docker:
	$(MANAGE) migrate
	$(MANAGE) collectstatic --noinput
	$(MANAGE) create_superuser
	$(MANAGE) init_countries
	gunicorn --workers=3 --timeout=120 config.wsgi -b 0.0.0.0:8000 --reload

docker-run:
	docker-compose -f docker-compose.yml up --build

docker-down:
	docker-compose -f docker-compose.yml down


# Celery command
worker:
	celery -A config.celery worker -l info

purge:
	celery -A config.celery purge
