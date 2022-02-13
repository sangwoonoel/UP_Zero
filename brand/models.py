from django.db import models
from users.models import *

class Brand(models.Model):
    name = models.CharField('브랜드명', max_length=20)
    category = models.ForeignKey('Category', verbose_name='카테고리', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', verbose_name='태그', blank=True)
    desc = models.CharField('소개', max_length=100)
    info = models.TextField('설명')
    image = models.ImageField('이미지', upload_to='brand/')
    link = models.URLField('링크')

    def __str__(self):
        return self.name


class BrandLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}님의 {self.brand.name} 좋아요 기록'


class Category(models.Model):
    name = models.CharField('영문 카테고리명', max_length=20) # 나중에 지우기
    name_ko = models.CharField('국문 카테고리명', max_length=20)

    def __str__(self):
        return self.name_ko


class Tag(models.Model):
    name = models.CharField('태그명', max_length=20)

    def __str__(self):
        return self.name