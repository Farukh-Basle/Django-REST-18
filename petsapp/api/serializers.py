
from rest_framework import serializers
from petsapp.models import Account

from django.conf  import settings
from django.contrib.auth.hashers import make_password

class AccountRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('first_name','last_name','username','email','mobile',
                   'password','role_type','image')

    def create(self, validated_data):
        account = Account.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            mobile = validated_data['mobile'],

            password = make_password(validated_data['password'],
                                     salt=settings.SECRET_KEY),

            role_type = validated_data['role_type'],
            image = validated_data['image'],
        )
        account.save()
        return account




