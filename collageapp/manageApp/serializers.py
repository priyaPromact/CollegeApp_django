from rest_framework import serializers
from manageApp.models import collegeAppUser,MainCategories,UserCategoryLink

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