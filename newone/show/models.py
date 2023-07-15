from django.db import models

# Create your models here.
class show(models.Model):
    names=models.CharField(max_length=100)
    addresss=models.TextField()
    emails:models.CharField(max_length=100)
    rollnum:models.IntegerField()
    
