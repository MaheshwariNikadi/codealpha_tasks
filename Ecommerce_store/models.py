from django.db import models


# 📦 PRODUCT MODEL
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


# 🧾 ORDER MODEL
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"Order {self.id}"


# 📦 ORDER ITEMS MODEL
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"