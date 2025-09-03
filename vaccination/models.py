from django.db import models
from animals.models import Animal

class Vaccination(models.Model):
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    next_due_date = models.DateField(null=True, blank=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="vaccinations")

    def __str__(self):
        return f"{self.vaccine_name} for {self.animal.name}"

