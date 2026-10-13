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

    name = models.CharField
    size = models.CharField(choices=sizechoice)
    friendliness = models.IntegerField(validators=rating)
    trainability = models.IntegerField(validators=rating)
    sheddingamount = models.IntegerField(validators=rating)
    exerciseneeds = models.IntegerField(validators=rating)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    gender = models.CharField
    color = models.CharField
    favoritefood = models.CharField
    favoritetoy = models.CharField

    def __str__(self):
        return self.name