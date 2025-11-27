# pets/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    
    validators = [MinValueValidator(1), MaxValueValidator(5)]
    friendliness = models.IntegerField(validators=validators)
    trainability = models.IntegerField(validators=validators)
    sheddingamount = models.IntegerField(validators=validators)
    exerciseneeds = models.IntegerField(validators=validators)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed, 
        on_delete=models.CASCADE, 
        related_name="dogs"
    )
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name