# Generated by Django 3.2.5 on 2021-07-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_content_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='city_or_village',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]