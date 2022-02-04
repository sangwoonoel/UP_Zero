from django.db import models
from users.models import *

class Brand(models.Model):
    name = models.CharField("브랜드명", max_length=20)
    # category
    image = models.ImageField("브랜드 이미지", upload_to="brand/")
    info = models.TextField("브랜드 소개")
    link = models.URLField("브랜드 링크")

class BrandLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)