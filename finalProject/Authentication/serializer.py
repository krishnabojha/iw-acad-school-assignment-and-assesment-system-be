from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserLoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name', 'email', 'password']
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key','user_id']

class UserSignUpModelSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
# password reset serializer
class ResetUserpasswordModelSerializer(serializers.Serializer):
    newpassword = serializers.CharField()
    class Meta:
        model = User
        fields = ['newpassword']

class OTPModelSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otpcode = serializers.IntegerField()
    class Meta:
        fields = ['email', 'otpcode']
