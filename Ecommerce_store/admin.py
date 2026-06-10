from django.contrib import admin
from .models import Product, Order, OrderItem


# 📦 Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


# 🧾 Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'created_at')


# 📦 OrderItem Admin
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')


# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)