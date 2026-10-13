from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Breed(models.Model):
    size_choice = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    rating = [MinValueValidator(1), MaxValueValidator(5)]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=size_choice)
    friendliness = models.IntegerField(validators=rating)
    trainability = models.IntegerField(validators=rating)
    sheddingamount = models.IntegerField(
        validators=rating,
        verbose_name="shedding amount"
    )
    exerciseneeds = models.IntegerField(
        validators=rating,
        verbose_name="exercise needs"
    )
    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name