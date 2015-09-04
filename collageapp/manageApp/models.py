import hashlib
from django.db import models


class collegeAppUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password).hexdigest()
        super(collegeAppUser, self).save(*args, **kwargs)

class MainCategories(models.Model):
    category_name = models.CharField(max_length=100)

class College(models.Model):
    college_name = models.CharField(max_length=250)
    college_url = models.CharField(max_length=500)

class UserCollegeLink(models.Model):
    user = models.ForeignKey(collegeAppUser)
    college = models.ForeignKey(College)

class UserCategoryLink(models.Model):
    user = models.ForeignKey(collegeAppUser)
    cat = models.ForeignKey(MainCategories)

class CollegeCategoryLink(models.Model):
    college_id = models.ForeignKey(College)
    category_id = models.ForeignKey(MainCategories)

