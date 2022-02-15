# Generated by Django 4.0.2 on 2022-02-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_alter_brand_desc_alter_brand_image_alter_brand_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ko',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='카테고리명'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
