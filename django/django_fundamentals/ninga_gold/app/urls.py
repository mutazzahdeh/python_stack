from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.home),
    url('process_money$', views.process),
    url('reset', views.reset),
]