from django.contrib import admin
from .models import Good, Client, Order

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name']
    list_filter = ['price']

    fields = ['name', 'desc', 'price', 'quantity']
    readonly_fields = ['name', 'price']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']
    ordering = ['name']

    fields = ['name', 'email', 'phone_number', 'address']
    readonly_fields = ['email']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'get_good', 'total_price', 'order_date']
    ordering = ['order_date']

    fields = ['client', 'total_price', 'order_date']
    readonly_fields = ['client']