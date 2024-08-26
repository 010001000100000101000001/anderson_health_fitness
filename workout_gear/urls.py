from django.urls import path
from . import views

urlpatterns = [
    path('', views.gear_list, name='gear_list'),
    path('<int:item_id>/', views.gear_detail, name='gear_detail'),
    path('category/<int:category_id>/', views.category_gear_list, name='category_gear_list'),
]
