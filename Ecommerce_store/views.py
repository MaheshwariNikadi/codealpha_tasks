from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem


# 📄 PRODUCT DETAILS PAGE
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {"product": product})


# 🛒 ADD TO CART (SESSION BASED)
def add_to_cart(request, id):
    cart = request.session.get("cart", {})

    # increase quantity if already exists
    cart[str(id)] = cart.get(str(id), 0) + 1

    request.session["cart"] = cart
    return redirect("cart")


# 🛒 CART PAGE
def cart(request):
    cart = request.session.get("cart", {})

    products = Product.objects.filter(id__in=cart.keys())

    items = []
    total = 0

    for product in products:
        qty = cart[str(product.id)]
        total += product.price * qty

        items.append({
            "product": product,
            "qty": qty
        })

    return render(request, "cart.html", {
        "items": items,
        "total": total
    })


# 📦 CHECKOUT / ORDER PROCESSING
def checkout(request):
    cart = request.session.get("cart", {})

    # If cart is empty
    if not cart:
        return render(request, "checkout.html", {"order": None})

    if request.method == "POST":
        order = Order.objects.create(total_price=0)

        total = 0

        for pid, qty in cart.items():
            product = Product.objects.get(id=pid)

            total += product.price * qty

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty
            )

        order.total_price = total
        order.save()

        # clear cart after order
        request.session["cart"] = {}

        return render(request, "checkout.html", {"order": order})

    return render(request, "checkout.html", {"order": None})