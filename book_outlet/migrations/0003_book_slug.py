# Generated by Django 3.2.5 on 2021-08-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_auto_20210823_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
