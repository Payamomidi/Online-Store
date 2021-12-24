from django.db import models
from product.models import Goods
from userprofil.models import Coustomer

class Cart(models.Model):
    user = models.ForeignKey(Coustomer, on_delete=models.CASCADE)
    item = models.ForeignKey(Goods, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField()
    price_total = models.CharField(max_length=50)
    creat_date = models.DateTimeField()
    update_date = models.DateTimeField()


class CartItem(models.Model):
    item = models.ForeignKey(Goods, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField()


class CheckOut(models.Model):
    user = models.OneToOneField(Cart, on_delete=models.CASCADE)
    payment = models.BooleanField()
    address = models.CharField(max_length=700)
    orderd = models.BooleanField()
    payment_date = models.DateTimeField()