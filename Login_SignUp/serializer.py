from dataclasses import fields
import imp
from rest_framework import serializers
from .models import *


class LoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginModel
        fields = (
            'username',
            'password'
        )
