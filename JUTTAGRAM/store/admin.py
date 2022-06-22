from django.contrib import admin
from django.contrib.auth.models import Group
from store.models import Category, Product, Cart

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.unregister(Group)
admin.site.register(Cart)

