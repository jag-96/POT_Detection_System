from django.urls import path

from . import views

urlpatterns = [
    path('', views.List, name='List'),
    path('edit_data_delete/', views.edit_data_delete, name='edit_data_delete'),
    path('edit_data_add/', views.edit_data_add, name='edit_data_add'),
    path('edit_data_update/', views.edit_data_update, name='edit_data_update'),
    path('test/', views.test, name='test'),
]