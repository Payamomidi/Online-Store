
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model
from django.db.models.manager import Manager

User = get_user_model()

class Coustomer(User):
    
    #username = models.CharField(max_length=35)
    #password = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    phone_namber = models.CharField(max_length=11)
    address = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Coustomer"


    def __str__(self) -> str:
        return self.name