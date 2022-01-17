from turtle import update
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


class UserProfilesManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password):
        if not username:
            raise ValueError("Users must have a username")

        elif not first_name:
            raise ValueError("Users must have a first_name")

        elif not last_name:
            raise ValueError("Users must have a last_name")

        elif not email:
            raise ValueError("Users must have a email")

        user = self.model(username=username,
                          first_name=first_name, last_name=last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password):
        if not username:
            raise ValueError("Users must have a username")

        elif not first_name:
            raise ValueError("Users must have a first_name")

        elif not last_name:
            raise ValueError("Users must have a last_name")

        elif not email:
            raise ValueError("Users must have a email")

        elif not password:
            raise ValueError("Users must have a password")

        user = self.create_user(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class UserProfiles(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_to)
    company = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    program_of_study = models.CharField(max_length=100)

    objects = UserProfilesManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        return self.username
