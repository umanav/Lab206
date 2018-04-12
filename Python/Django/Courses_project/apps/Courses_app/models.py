# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        name = postData.get('name')
        description = postData.get('description')
        errors = []
        if len(name) < 5:
            errors.append("The 'Name' has to be more than 5 characters long")
        if len(description) < 15:
            errors.append("The 'Description' has to be more than 15 characters long")
        return errors


class Course(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField(null=True)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = CourseManager()