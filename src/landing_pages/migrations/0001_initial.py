# Generated by Django 5.1.4 on 2025-02-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=85)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
