from django.db import models
from django.contrib.auth.models import AbstractUser

# Restaurant menu 
class Category(models.Model):
    name = models.CharField(max_length=30)
    footer = models.TextField(blank=True)

class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=120, blank=True)
    price = models.CharField(max_length=8) #no calculations with this item
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    
class SetMenu(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price=models.CharField(max_length=8) #no calculations with this item
    
# Contact
class Customer(AbstractUser):
    phoneNumber = models.CharField(max_length = 16, unique = True)
    
class Reservation(models.Model):
    date = models.DateField(null=False)
    pax = models.IntegerField(null=False, blank=False)
    hour = models.TimeField(null=False, blank=False)
    comment = models.TextField(null=False, blank=True, max_length=1200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'my_reservations')

    def __str__(self):
        return f'{self.date} , {self.customer} , {self.hour} ,{self.customer.phoneNumber}, {self.comment}'

    
    