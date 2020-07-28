from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(help_text="Acerca del producto.")
    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name