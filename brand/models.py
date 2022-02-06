from django.db import models
from users.models import *

class Brand(models.Model):
    name = models.CharField('브랜드명', max_length=20)
    # category
    image = models.ImageField('브랜드 이미지', upload_to='brand/')
    info = models.TextField('브랜드 소개')
    link = models.URLField('브랜드 링크')

    def __str__(self):
        return self.name

class BrandLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}님의 {self.brand.name} 좋아요 기록'