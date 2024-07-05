from django.db import models
from django.core.validators import MinValueValidator

class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption

class Producto(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=True, blank=True)
    carbs = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, validators=[MinValueValidator(0)])
    fat = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, validators=[MinValueValidator(0)])
    protein = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, validators=[MinValueValidator(0)])
    salt = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True, validators=[MinValueValidator(0)])
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False, validators=[MinValueValidator(0)])
    stock = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name