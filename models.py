from django.db import models

# Create your models here.
class ProductData(models.Model):
    product_id=models.IntegerField()
    product_type=models.CharField(max_length=30)
    product_cost=models.IntegerField()
    product_class=models.CharField(max_length=20)#high/low/mediun
    product_color=models.CharField(max_length=20)
    brand_name=models.CharField(max_length=20)
    organisation_mobile=models.BigIntegerField()
    organisation_email=models.EmailField(max_length=100)