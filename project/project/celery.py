import os
from celery import  Celery
from celery import shared_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
app = Celery("project")
app.config_from_object("django.conf:settings", namespace="CELERY")

# tasks
# @app.task
# def add_numbers(x, y):
#     return x + y

@shared_task
def add_numbers(x, y):
    return x + y

app.autodiscover_tasks()