from django.db import models

class Users(models.Model):
    oAuthID = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class MainCategories(models.Model):
    category_name = models.CharField(max_length=100)

class College(models.Model):
    category_id = models.ForeignKey(MainCategories)
    college_name = models.CharField(max_length=250)
    college_url = models.CharField(max_length=500)

class UserCollegeLink(models.Model):
    user_id = models.ForeignKey(Users)
    college_id = models.ForeignKey(College)