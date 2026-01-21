from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
    

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("citizen", "Citizen"),
        ("municipality", "Municipality"),
        ("truck_operator", "Truck Operator"),
        ("factory", "Factory"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
