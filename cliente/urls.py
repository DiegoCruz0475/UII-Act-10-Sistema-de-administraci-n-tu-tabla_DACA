from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:id>', views.ver_clientes, name='ver_clientes'), 
    path('add/', views.add, name='add'), 
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete_cliente, name='delete'),
    path('delete/success/', views.delete_success, name='delete_success'),
]