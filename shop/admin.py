from django.contrib import admin

# Register your models here.

from .models import Product_des,Contact,Order

admin.site.register(Product_des)
admin.site.register(Contact)
admin.site.register(Order)

