
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addd', views.adddojo),
    path('addn', views.addninja),
]
