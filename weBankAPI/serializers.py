from rest_framework import serializers
from .models import Accounts
from .models import *
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['firstname', 'lastname', 'account_no', 'account_type']
        
class AccountCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['firstname', 'lastname', 'account_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
class EmailVerification(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'otp']
        
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['accounts_id', 'amount', 'transaction_type']


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
