from django.forms import models
from rest_framework import serializers
from .models import UserProfiles


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'image'
        )
