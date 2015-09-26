from rest_framework import serializers
from manageApp.models import collegeAppUser,MainCategories,UserCategoryLink, CollegeCategoryLink, College, UserCollegeLink

class collegeAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = collegeAppUser
        fields = ('id', 'username', 'password')

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategories
        fields = ('id', 'category_name')

class UserCategoryLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategoryLink
        fields = ('id', 'user', 'cat')

class CollegeCategoryLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeCategoryLink
        fields = ('id', 'college_id', 'category_id')

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'college_name', 'college_url')

class UserCollegeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollegeLink
        fields = ('id', 'user', 'college')