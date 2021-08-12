from django.db import models

# Create your models here.

class Art(models.Model):
    name = models.CharField(max_length=250)
    file = models.FileField()
    file_frame = models.FileField()
    shopurl = models.CharField(max_length=250,default="https://www.etsy.com/uk/shop/MathematicalArtShop")
    description = models.CharField(max_length=1000, default='Add description here...')

    def __str__(self):
        return self.name
