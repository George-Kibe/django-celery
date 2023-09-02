from django.contrib import admin
from django.urls import path, include
from notifications.consumers import NotificationsConsumer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notifications.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

websocket_urlpatterns = [
    path("ws/notifications/", NotificationsConsumer.as_asgi()),
]