from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('createClients/', views.create_clients, name='create_clients'),
    path('getClient/', views.get_client, name='get_client'),
    path('getAllClients/', views.get_all_client, name='get_all_clients'),
    path('updateClients/', views.update_client_name, name='update_client'),
    path('deleteClient/', views.delete_client, name='delete_client'),
    path('createGoods/', views.create_goods, name='create_goods'),
    path('createOrders/', views.create_orders, name='create_orders'),
    path('getClientOrders/<int:id>/', views.get_client_orders, name='get_client_orders'),
    path('product_add/', views.add_product_manually, name='add_product_manually'),
]