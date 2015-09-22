from django.contrib import admin
from .models import collegeAppUser, MainCategories, College, UserCollegeLink, UserCategoryLink, CollegeCategoryLink

# Register your models here.
admin.site.register(collegeAppUser)
admin.site.register(MainCategories)
admin.site.register(College)
admin.site.register(UserCollegeLink)
admin.site.register(UserCategoryLink)
admin.site.register(CollegeCategoryLink)