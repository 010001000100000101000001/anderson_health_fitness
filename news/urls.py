from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('post/<int:post_id>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news_post, name='add_news_post'),
    path('edit/<int:post_id>/', views.edit_news_post, name='edit_news_post'),
]
