from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

