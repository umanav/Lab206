# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class ninjas(models.Model):
    dojo_id = models.ForeignKey(dojos, related_name="ninjas") 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class desc(models.Model):
    text = models.TextField()