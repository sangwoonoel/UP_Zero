from django.db import models
from users.models import *




class BrandLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
# Create your models here.

