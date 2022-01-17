from unittest import mock
from django.db import models


class menteeRowInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    numLeetCode = models.IntegerField()
    jobRole = models.CharField(max_length=20)
    linkedLink = models.URLField()
    leetcodeLink = models.URLField()
    skills = models.CharField(max_length=500)
    projects = models.CharField(max_length=500)
    jobId = models.CharField(max_length=20)
    jobDescriptionLink = models.URLField()

    def __str__(self) -> str:
        return self.jobRole
