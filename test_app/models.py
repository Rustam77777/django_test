from django.db import models

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        related_name='products'
    )
