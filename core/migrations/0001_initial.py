# Generated by Django 5.1.2 on 2024-12-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('province', models.CharField(max_length=255)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('event_organizer', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
