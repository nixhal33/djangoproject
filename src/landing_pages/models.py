from django.db import models

# Create your models here.

class LandingPageEntry(models.Model):
    name=models.CharField(max_length=85)
    email=models.EmailField()