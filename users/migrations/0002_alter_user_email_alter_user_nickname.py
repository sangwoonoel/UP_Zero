# Generated by Django 4.0.2 on 2022-02-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': '이미 등록된 이메일입니다.'}, max_length=254, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 존재하는 닉네임입니다.'}, max_length=10, null=True, unique=True, verbose_name='닉네임'),
        ),
    ]
