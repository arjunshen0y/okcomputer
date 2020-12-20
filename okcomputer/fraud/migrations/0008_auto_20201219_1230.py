# Generated by Django 3.1.3 on 2020-12-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0007_auto_20201219_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='new_balance_dest',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='new_balance_org',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='old_balance_dest',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='old_balance_org',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transfer_type',
            field=models.CharField(choices=[('cashout', 'CASH OUT'), ('payment', 'PAYMENT'), ('cashin', 'CASH IN'), ('transfer', 'TRANSFER'), ('debit', 'DEBIT')], default='cashout', max_length=256),
        ),
    ]
