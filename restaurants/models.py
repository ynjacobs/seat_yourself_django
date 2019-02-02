from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_restaurants')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='restaurants')
    guests = models.ManyToManyField(User, through='Reservation', related_name='reserved_restaurants')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    capacity = models.IntegerField()
    image = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, related_name='reservations_made', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, related_name='reservations', on_delete=models.CASCADE)
    party_size = models.IntegerField()
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return "{} - party of {}".format(self.datetime, self.party_size)

