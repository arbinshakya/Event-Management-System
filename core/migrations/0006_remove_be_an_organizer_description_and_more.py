# Generated by Django 5.1.2 on 2024-12-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_be_an_organizer_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='be_an_organizer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='be_an_organizer',
            name='event_type',
        ),
        migrations.AddField(
            model_name='be_an_organizer',
            name='organization_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
