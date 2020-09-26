from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    admin=models.BooleanField()
    phno=models.IntegerField()
    password=models.TextField(max_length=10)


class Products(models.Model):
    productname=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    quantity=models.IntegerField()
    donatorname=models.CharField(max_length=100)
    donator_phno=models.IntegerField()
    donatoremail=models.EmailField(max_length=400)
    donator_address=models.TextField()

class ProductQuery(models.Model):
    productname=models.CharField(max_length=100)
    request=models.TextField(max_length=300)
    quantity_needed=models.IntegerField()
    reciever_name=models.CharField(max_length=100)
    reciever_phno=models.IntegerField()
    recieveremail=models.EmailField(max_length=400)
    reciever_address=models.TextField()
    neededBy=models.DateField()
