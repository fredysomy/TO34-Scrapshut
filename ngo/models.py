from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    admin=models.BooleanField()
    phno=models.IntegerField(max_length=10)
    