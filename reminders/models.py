from django.db import models
from animals.models import Animal

class Reminder(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="reminders")
    message = models.CharField(max_length=255)
    reminder_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.animal.name} on {self.reminder_date}"

