from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("User must have a valid username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    city = models.CharField(max_length=30, null=True, blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = []
      


class Info(models.Model):
    city = models.CharField(max_length=50)
    temp = models.FloatField()
    weather_report = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    humidity = models.IntegerField()
    pressure = models.IntegerField()