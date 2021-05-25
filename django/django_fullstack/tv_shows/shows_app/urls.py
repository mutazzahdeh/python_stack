from django.urls import path
from . import views

urlpatterns = [
   path('shows',views.index),
   path('show/<int:show_id>',views.view_show),
   path('shows/new',views.new),
   path('add_show',views.add_show),
   path('show/<int:show_id>/edit',views.edit_show),
   path('edit/<int:show_id>',views.edit),
   path('delete/<int:show_id>',views.delete),

]