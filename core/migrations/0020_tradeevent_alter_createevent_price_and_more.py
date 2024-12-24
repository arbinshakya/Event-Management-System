# Generated by Django 5.1.2 on 2024-12-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_createevent_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('buyer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='createevent',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='total_ticket',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]