# Generated by Django 5.2.1 on 2025-06-18 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_status', models.IntegerField(choices=[(0, 'done'), (1, 'pending'), (2, 'canceled')], default=1)),
                ('payment_method', models.IntegerField(choices=[(1, 'stripe'), (2, 'paypal')], null=True)),
                ('transaction_id', models.CharField(blank=True, help_text='Transaction number from payment gateway (webhook)', max_length=100, null=True, unique=True)),
                ('session', models.CharField(blank=True, max_length=255, null=True)),
                ('items', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.OneToOneField(help_text='For the payment related to this date', on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='clinic.appointment')),
            ],
        ),
    ]
