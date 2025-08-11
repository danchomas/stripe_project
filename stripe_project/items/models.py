from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(
        validators=[MinValueValidator(50)],
        help_text="цена в центах, не меньше 50"
    )

    def __str__(self):
        return self.name

    @property
    def price_dollars(self):
        return self.price / 100
