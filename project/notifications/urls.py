from django.urls import path
from .views import notification_page_view

urlpatterns = [
    path('', notification_page_view, name='notifications'),
]

