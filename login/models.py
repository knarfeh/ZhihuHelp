from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LoginRecord(models.Model):
    account    = models.CharField(max_length=200)
    password   = models.CharField(max_length=200)
    recordDate = models.DateField(auto_now=True)
    cookie     = models.TextField()
    