from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    date = models.DateField()
    distance = models.FloatField(validators=[MinValueValidator(0.1)])
    duration = models.FloatField(validators=[MinValueValidator(0.1)])
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date)

    def get_average_speed(self):
        average_speed = self.distance / self.duration
        return average_speed
