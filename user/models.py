from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=20)
    df = models.CharField(max_length=15)

    def __str__(self):
        return self.city + " " + self.df

class Event(models.Model):

    MODALITY_CHOICES = (
        ('fr','Free'),
        ('pd','Paid')
    )

    TYPE_EVENT_CHOICES = (
        ('p', 'Rolê Pequeno'),
        ('m', 'Rolê Médio'),
        ('g', 'Moster grande porte')
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    king = models.IntegerField(null=True)
    modality = models.CharField(max_length=2, choices=MODALITY_CHOICES, blank=True, null=True)
    forbidden = models.BooleanField(default = False)
    drinks = models.BooleanField(default = False)
    type = models.CharField(max_length=2, choices=TYPE_EVENT_CHOICES, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    capacity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='event_logo/', default='event_logo/default.jpg')

    def __str__(self):
        return self.name

class User_animal(models.Model):

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    type = models.CharField(max_length=6, blank=True, null=True)
    address = models.OneToOneField(Address, related_name="address", on_delete=models.CASCADE, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='clients_photos/', default='clients_photos/default.jpg')



    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

