# Generated by Django 2.2.1 on 2019-05-27 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20190527_0333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='person_id',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='monthly_payment_id',
            new_name='monthly_payment',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='loan_id',
            new_name='loan',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='property_type_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='property_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='landing.Property'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
