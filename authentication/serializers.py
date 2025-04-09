from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'MyUserSerializer'  # نام مرجع را به طور صریح تنظیم کنید

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

#
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
#         ref_name = 'MyCustomUserSerializer'
#         extra_kwargs = {'password': {'write_only': True}}
#