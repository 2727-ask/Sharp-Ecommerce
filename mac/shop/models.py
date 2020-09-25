from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_say = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc=models.TextField(null=True,blank=True)
    product_img=models.ImageField(null=True)
    product_img_1=models.ImageField(null=True)
    product_img_2=models.ImageField(null=True)
    product_img_3=models.ImageField(null=True)
    product_img_4=models.ImageField(null=True)
    brand_name=models.CharField(max_length=20,null=True)
    brand_image=models.ImageField(null=True)
    def __str__(self):
            return self.product_name

class Ads(models.Model):
    ad_id = models.AutoField(primary_key=True)
    ad_name=models.CharField(max_length=50)
    ad_say=models.CharField(max_length=500,null=True)
    ad_img1=models.ImageField(upload_to='shop/images')


    def __str__(self):
        return self.ad_name

class Orders(models.Model):

    order_id=models.AutoField(primary_key=True)
    cart_products =models.CharField(max_length=10000)
    amount =models.IntegerField(default=0)
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    address=models.CharField(max_length=700)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    zip_code=models.IntegerField()
    mail=models.CharField(max_length=200)
    phone1=models.IntegerField()
    phone2=models.IntegerField()

    def __str__(self):
        return self.fname


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0::7]+"...."


class Product_Rating(models.Model):
    product_id = models.AutoField(primary_key=True)
    cust_fname = models.CharField(max_length=50)
    cust_lname = models.CharField(max_length=50)
    cust_email = models.CharField(max_length=150)
    review = models.CharField(max_length=1500,null=True)
    star = models.IntegerField(default=1)
    prod_name = models.CharField(max_length=100,null=True)
    timestamp = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.prod_name


