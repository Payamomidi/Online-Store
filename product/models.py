from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=50)


class Goods(models.Model):
    title = models.CharField(max_length=50)
    brand = models.ManyToManyField(Brand)
    goods_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    price = models.CharField(max_length=50)
    amount = models.IntegerField()
    
