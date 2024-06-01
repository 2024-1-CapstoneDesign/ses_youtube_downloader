from .views import *
from django.urls import path, include

urlpatterns = [
    path("google/login/", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
]
