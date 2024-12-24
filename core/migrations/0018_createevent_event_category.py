# Generated by Django 5.1.2 on 2024-12-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_ticket_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='createevent',
            name='event_category',
            field=models.CharField(choices=[('concert', 'Concert'), ('trade', 'Trade')], default='concert', max_length=255),
        ),
    ]