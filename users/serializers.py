from rest_framework import serializers
from .models import Userprofile
class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['email']

class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['email','otp','password']