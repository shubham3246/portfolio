# Generated by Django 4.2 on 2024-03-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0010_alter_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='protfolio/static/footer_profile/'),
        ),
        migrations.AlterField(
            model_name='cerficate',
            name='image',
            field=models.ImageField(upload_to='media/certificates/'),
        ),
    ]
