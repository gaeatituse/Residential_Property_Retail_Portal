from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    # Add any additional fields or methods as needed

    def __str__(self):
        return self.user.username
