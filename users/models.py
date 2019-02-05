from django.db import models
from django.contrib.auth.models import User

class createUser(models.Model):
    userType = models.CharField(max_length=12)
    username = models.CharField(max_length=100)


    def __str__(self):
        return self.username
