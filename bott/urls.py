from django.urls import path
from django.views.decorators.http import require_GET, require_POST
from .import views



urlpatterns = [
    path('',views.home , name='home'),
    path('verify_webhook/', require_GET(views.webhook_get), name='webhook_get'),
    path('webhook/', require_POST(views.webhook_post), name='webhook_post'),
]