# Generated by Django 4.2 on 2024-03-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0007_project_best_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('video_link', models.CharField(blank=True, max_length=500, null=True)),
                ('channel_link', models.CharField(max_length=500)),
            ],
        ),
    ]
