.PHONY: run-server superuser build migrate down interact change-mode run-uvicorn

migrate:
	python3 manage.py makemigrations; python3 manage.py migrate

run-server:
	python3 manage.py runserver

superuser:
	python3 manage.py createsuperuser

build:
	docker-compose up -d --build

down:
	docker-compose down --remove-orphans

interact:
	docker exec -it django  /bin/sh
	# django is the name of the container

change-mode:
	chmod +x ./entrypoint.sh

run-uvicorn:
	uvicorn project.asgi:application --port 8000 --workers 4 --log-level debug --reload