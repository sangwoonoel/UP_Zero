from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=10, unique=True, null=True)
    email = models.EmailField('이메일', unique=True)
    image = models.ImageField('프로필 이미지', default='logo.png', upload_to='users/', null=True)

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.username