from django.db import models

# Create your models here.

"""
Whenever you make changes in this model.py file you always run these 2 commands
1. python manage.py makemigrations
2. python manage.py migrate

Why?
so that your database and model alway synced up..!! :)
"""

class LandingPageEntry(models.Model):
    name=models.CharField(max_length=85, blank=False, null=False)
    email=models.EmailField()
    password=models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}" # i can change this self.name into self.email where i can see changes in the admin panel where it will show email of those LandingpageEntry as name of entrants
     