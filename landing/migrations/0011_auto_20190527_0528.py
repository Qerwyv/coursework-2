# Generated by Django 2.2.1 on 2019-05-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_record_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_payment',
            name='expiration_payment',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='monthly_payment',
            name='monthly_payment',
            field=models.FloatField(),
        ),
    ]