# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    creditCard = models.CharField(max_length=16, null= True)
    shipping_street_address = models.CharField(max_length=255, null=True)
    shipping_city = models.CharField(max_length=255, null=True)
    shipping_state = models.CharField(max_length=2, null=True)
    shipping_country = models.CharField(max_length=50, null=True)
    billing_street_address = models.CharField(max_length=255, null=True)
    billing_city = models.CharField(max_length=255, null=True)
    billing_state = models.CharField(max_length=2, null=True)
    billing_country = models.CharField(max_length=50, null=True)
  
    # objects = UserManager()
    def __str__(self):
        return "{} {} {} {}".format(self.name, self.username, self.email, self.password) 

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField() # for contacting the vendor, about specific product questions
    vendorType = models.CharField(max_length=20) # localArtist, brand, charity
    bio = models.CharField(max_length=255)  # vendor short bio.


class Band(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    imageUrl = models.CharField(max_length=255)
    vendor = models.ForeignKey('Vendor', related_name = "bands")
    
    def __str__(self):
        return "{} {}".format(self.name, self.creator.name) 

class Order(models.Model):
    bands = models.ManyToManyField(Band)
    user = models.ForeignKey('user', related_name = "orders")
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date created')