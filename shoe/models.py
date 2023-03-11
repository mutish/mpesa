from django.db import models

# Create your models here.
class Shoes(models.Model):
    Shoe_name = models.CharField(max_length=100)
    Shoe_image = models.CharField(max_length=100000)
    Shoe_price = models.CharField(max_length=100)

    class Meta:
        db_table = 'shoe'










