from django.urls import path
from . import views

urlpatterns = [
    path('', views.gear_list, name='gear_list'),
    path('<int:item_id>/', views.gear_detail, name='gear_detail'),
    path('category/<int:category_id>/', views.category_gear_list, name='category_gear_list'),
    path('search/', views.search_gear, name='search_gear'),
    path('gear/<int:item_id>/review/', views.submit_review, name='submit_review'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:item_id>/', views.edit_product, name='edit_product'),
]
