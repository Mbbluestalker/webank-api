# Generated by Django 4.0.4 on 2022-04-26 22:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weBankAPI', '0002_transaction_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('account_type', models.CharField(choices=[('SAVINGS', 'savings'), ('CURRENT', 'current')], max_length=40)),
                ('account_balance', models.FloatField(default=0)),
            ],
        ),
    ]
