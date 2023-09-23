from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    publication_year = models.IntegerField(default=1700, validators=[MaxValueValidator(2023), MinValueValidator(1700)])

    def __str__(self):
        return f'{self.title} {self.author}'
    