from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.create_blogpost, name='record'),
    path('show/',views.show_students, name='show'),
    path('show_results/', views.show_results, name='show_results'),
    path('registration/', views.registration, name='registration'),
    path('new_group/', views.group_registration, name='group_registration'),
]
