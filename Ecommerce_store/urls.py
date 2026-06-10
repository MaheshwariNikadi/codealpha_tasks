from django.urls import path
from . import views

urlpatterns = [
    # 📄 Product Detail Page
    path("product/<int:id>/", views.product_detail, name="product_detail"),

    # 🛒 Cart Operations
    path("add/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),

    # 📦 Order Processing
    path("checkout/", views.checkout, name="checkout"),
]