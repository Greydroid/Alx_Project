from django.db import models
from users.models import User   

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100,  null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="animals")

    def __str__(self):
        return f"{self.name} ({self.species})"


