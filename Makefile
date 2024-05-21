# Definition
MANAGE = python manage.py
SOURCE = src

# Commands

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


start-docker:
	$(MANAGE) migrate
	$(MANAGE) collectstatic --noinput
	$(MANAGE) create_superuser
	gunicorn --workers=3 --timeout=120 config.wsgi -b 0.0.0.0:8000 --reload

docker-run:
	docker-compose -f docker-compose.yml up --build

docker-down:
	docker-compose -f docker-compose.yml down


