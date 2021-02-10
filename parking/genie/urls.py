from django.urls import path

# import the views in the views.py file
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        ]
