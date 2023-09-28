from django.db import models

# Create your models here.
class Place(models.Model):

    nam=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()

    def __str__(self):
         return self.nam

class Person(models.Model):
    nam=models.CharField(max_length=250)
    img=models.ImageField(upload_to="perpic")
    desc=models.TextField()

    def __str__(self):
        return self.nam