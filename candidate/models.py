from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    """database for candidate information"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} with {self.phone_number} belong to {self.user.username}"
