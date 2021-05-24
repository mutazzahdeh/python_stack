from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('books/<int:number>', views.bookdesc),
    path('addaut', views.addaut),
]

