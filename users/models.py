from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=10, unique=True, null=True, error_messages={
            'unique': _('이미 존재하는 닉네임입니다.'),
        })
    email = models.EmailField('이메일', unique=True, error_messages={
            'unique': _('이미 등록된 이메일입니다.'),
        })
    image = models.ImageField('프로필 사진', default='logo.png', upload_to='users/', null=True)

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.username