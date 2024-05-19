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




