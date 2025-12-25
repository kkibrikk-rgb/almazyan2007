from django.db import models

class Cloth(models.Model):
    brand = models.CharField(max_length=100)
    size = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"Бренд: {self.brand}, Размер: {self.size}, Цена: {self.price}, Цвет: {self.color}"
    
