# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        password = postData.get('password')
        confirm_password = postData.get('confirm_password')
        errors = []
        if len(first_name) < 3:
            errors.append("first name needs more than 2 characters")
        elif not NAME_REGEX.match(first_name):
            errors.append("first name needs to have characters")
        if len(last_name) < 3:
            errors.append("last name needs more than 2 characters")
        elif not NAME_REGEX.match(last_name):
            errors.append("last name needs to have characters")
        if len(email) < 1:
            errors.append("email can't be empty")
        if not EMAIL_REGEX.match(email):
            errors.append("email must be valid")
        if len(password) < 9:
            errors.append("password needs more than 8 characters")
        if password != confirm_password:
            errors.append("passwords do not match")
        if errors == []:
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(first_name =first_name, last_name =last_name, email = email, password = password)
        return errors
    def login_validator(self, postData):
        email = postData.get('email')
        password = postData.get('password')
        errors = []
        if len(email) < 1:
            errors.append("email can't be empty")
        elif not EMAIL_REGEX.match(email):
            errors.append("email must be valid")
        try: 
            user = User.objects.get(email = email)
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return errors
            errors.append("password does not match")
        except User.DoesNotExist:
            errors.append("email is not registered")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

