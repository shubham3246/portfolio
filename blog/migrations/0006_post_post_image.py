# Generated by Django 3.2.4 on 2023-05-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230531_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='', upload_to='post'),
        ),
    ]
