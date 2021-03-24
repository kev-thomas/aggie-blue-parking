from django.urls import path

# import the views in the views.py file
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('login', views.login, name = "login"),
        path('rentals', views.getUserRentals, name = "rentals"),
        path('register', views.register, name = "register"),
        ]
