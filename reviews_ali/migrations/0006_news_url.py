# Generated by Django 3.2 on 2021-04-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_ali', '0005_auto_20210411_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.SlugField(default=1, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]