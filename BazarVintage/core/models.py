from django.db import models

# Create your models here.
class Product(models.Model):
    idProduct = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=False, default=0.00, null=False)
    stock = models.IntegerField(blank=False, null=False)
    description = models.TextField(max_length=150, blank=False, null=False)
    category_choices = [
        ('Madera', 'Madera'),
        ('Bazar', 'Bazar'),
        ('Deco', 'Deco'),
    ]
    category = models.CharField(max_length=100, choices=category_choices, blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True, default='products/default_image.jpg')
    sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name