from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=100)
    Position=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()