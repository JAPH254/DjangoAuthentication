from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=30)

def __str__(self):
    return self.name