# Generated by Django 5.1.2 on 2024-12-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_ticket_payment_completed_ticket_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('Khalti', 'Khalti')], max_length=20),
        ),
    ]