from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    room = models.CharField(max_length=20)
    description = models.TextField()
    additional_field = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    zarplata = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100, default="джуниор")
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    procient = models.DecimalField(max_digits=3, decimal_places=2)
    city = models.CharField(max_length=101, default="Узбекотатартаджикистан")


class CustomUser(AbstractUser):
    pass
    # class Event(models.Model):
    #     title = models.CharField(max_length=100)
    #     date = models.DateTimeField()
    #     description = models.TextField()
    #     cost = models.DecimalField(max_digits=10, decimal_places=2)
