from dataclasses import fields
from rest_framework import serializers
from .models import menteeRowInfo


class menteeRowInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = menteeRowInfo
        fields = (
            'id',
            'name',
            'numLeetCode',
            'jobRole',
            'linkedLink',
            'leetcodeLink',
            'skills',
            'projects',
            'jobId',
            'jobDescriptionLink'
        )
