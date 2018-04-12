# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        name = postData.get('name')
        email = postData.get('email')
        errors = {}
        if len(name) < 1:
            errors["name"] = "Name can't be empty"
            print errors
        if len(email) < 1:
            errors["email"] = "email can't be empty"
        elif not EMAIL_REGEX.match(email):
            errors["validEmail"] = "email must be valid"
        return errors

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


