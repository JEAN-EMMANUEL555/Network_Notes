from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='login'),
    path('home/', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('category/<int:category_id>/add/', views.add_command, name='add_command'),
    path('command/<int:command_id>/edit/', views.edit_command, name='edit_command'),
    path('category/add/', views.add_category, name='add_category'),
    path('command/<int:command_id>/delete/', views.delete_command, name='delete_command'),
    path('logout/', views.user_logout, name='logout'),
]
