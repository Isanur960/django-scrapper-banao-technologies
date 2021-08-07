from django.db import models

# Create your models here.


class ProductDB(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    link = models.TextField()
    img = models.TextField()
    price = models.CharField(max_length=20)
    detail = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.name
