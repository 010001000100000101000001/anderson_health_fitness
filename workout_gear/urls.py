from django.urls import path
from . import views

urlpatterns = [
    path('', views.gear_list, name='gear_list'),
]
