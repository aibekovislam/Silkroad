# Generated by Django 3.2.5 on 2021-07-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_silkroad_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
