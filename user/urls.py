from django.urls import path
from user.views import registration_view, logout
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("register/", registration_view, name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", logout, name="logout"),
]
