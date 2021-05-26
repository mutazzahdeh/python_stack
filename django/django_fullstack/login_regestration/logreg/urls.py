from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('logout',views.logouta),
    path('addn',views.welcome),
    path('suc',views.login),
]
