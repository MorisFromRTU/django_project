from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.create_blogpost, name='record'),
    path('show/',views.show_blogpost, name='show'),
    path('show_results/', views.show_results, name='show_results'),
]
