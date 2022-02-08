from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField("닉네임", max_length=10, unique=True)
    email = models.EmailField("이메일", unique=True)
    