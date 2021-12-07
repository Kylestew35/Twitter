from django.urls import path

from . import views

urlpatterns = [
    path('like/<int:post_id>/', views.like, name='like'),
    path('', views.index, name='index'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
]
