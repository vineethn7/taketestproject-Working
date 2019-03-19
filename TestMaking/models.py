from django.db import models

# Create your models here.
class Choices(models.Model):
    answers = models.CharField(max_length=10)
