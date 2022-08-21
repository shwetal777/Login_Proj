from django.db import models

# Create your models here.

class SignUp(models.Model):
    username= models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.username