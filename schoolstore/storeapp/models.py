from django.db import models

# Create your models here.
class Accomplishments(models.Model):
    name=models.CharField(max_length=50)
    disc=models.TextField()
    img=models.ImageField(upload_to='pics')

class Resources(models.Model):
    name2=models.CharField(max_length=50)
    disc2=models.TextField()
    img2=models.ImageField(upload_to='pics')