from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.name
