# Generated by Django 5.1.2 on 2024-12-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_alter_buyer_user_alter_seller_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
