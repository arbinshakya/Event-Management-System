# Generated by Django 5.1.2 on 2024-12-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_seller_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]