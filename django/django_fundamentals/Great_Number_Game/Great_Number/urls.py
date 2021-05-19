from django.urls import path 
from . import views
urlpatterns=[
    path("",views.index),
    path("submet",views.num),
    path("playagin",views.plyagine),
]