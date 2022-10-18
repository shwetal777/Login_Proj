from locale import currency
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.


class SignUp(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.username


class AccountsData(models.Model):
    name = models.CharField(max_length=100)
    account_no = models.IntegerField()
    account_balance = models.FloatField(max_length=100)
    currency = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}  |  {self.email}  |  {self.desc}  |  {self.date}"

