from django.db import models

# Create your models here.
class Valentine(models.Model):
    name=models.CharField(max_length=20,blank=False)
    crush=models.CharField(max_length=20,blank=False)
    score=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name
