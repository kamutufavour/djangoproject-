from __future__ import unicode_literals
from django.db import models


class students(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.Charfield(max_length=30)
    email=models.EmailField(max_length=35)
    class Meta:
         db_tablet="students"