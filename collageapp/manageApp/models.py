from django.db import models

class Users(models.Model):
    oAuthID = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)