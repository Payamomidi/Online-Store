from django.contrib import admin

from .models import Cart,CartItem,CheckOut


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CheckOut)
