from django.db import models

# Create your models here.
class Item (models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(decimal_places=2 , max_digits=10)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name