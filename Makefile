.PHONY: run-server superuser build migrate down interact change-mode

migrate:
	python3 project/manage.py makemigrations; python3 project/manage.py migrate

run-server:
	python3 project/manage.py runserver

superuser:
	python3 project/manage.py createsuperuser

build:
	docker-compose up -d --build

down:
	docker-compose down --remove-orphans

interact:
	docker exec -it django  /bin/sh
	# django is the name of the container

change-mode:
	chmod +x ./entrypoint.sh