# Generated by Django 4.0.2 on 2022-02-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0005_remove_brand_tag_remove_category_name_ko_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=10, verbose_name='카테고리명'),
        ),
    ]
