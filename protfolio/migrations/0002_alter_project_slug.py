# Generated by Django 4.2 on 2024-03-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]