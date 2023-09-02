from django.contrib import admin
from django.urls import path, include
from notifications.consumers import NotificationsConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notifications.urls")),
]

websocket_urlpatterns = [
    path("ws/notifications/", NotificationsConsumer.as_asgi()),
]