from django.db import models

# Create your models here.

class Product_des(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=1000,default="")
    pub_date = models.DateField()
    image_nm = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    con_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)
    msg = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemjson=models.CharField(max_length=1000)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")
    phone = models.IntegerField(default=0)
    country = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")
    zipcode = models.IntegerField(default=0)
    totall=models.CharField(max_length=150,default='')

    def __str__(self):
        return self.fname




