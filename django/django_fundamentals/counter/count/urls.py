from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('destoy', views.destroy2),
    path('addtow', views.add2),
    path('addnum', views.addnum),

]