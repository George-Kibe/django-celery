.PHONY: run-server superuser build migrate

migrate:
	python3 manage.py makemigrations; python3 manage.py migrate

run-server:
	python3 manage.py runserver

superuser:
	python3 manage.py createsuperuser

build:
docker-compose up -d --build

