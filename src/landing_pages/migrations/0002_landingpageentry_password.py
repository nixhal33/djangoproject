# Generated by Django 5.1.4 on 2025-02-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpageentry',
            name='password',
            field=models.CharField(default='default_password', max_length=128),
        ),
    ]
