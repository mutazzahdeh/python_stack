from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index),
    path('reg', views.registration),
    path('loginre', views.login),
    path('login', views.loginre),
    path('logout', views.logout),
    path('addmessage/<int:id>', views.addmessage),
    path('addcomment/<int:id_message>/<int:id_user>', views.addcomment),
    path('login/wall', views.wall),
]
