# Generated by Django 3.1.3 on 2020-12-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0004_auto_20201216_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cat',
            field=models.CharField(choices=[('cashout', 'CASH OUT'), ('payment', 'PAYMENT'), ('cashin', 'CASH IN'), ('transfer', 'TRANSFER'), ('debit', 'DEBIT')], default='cashout', max_length=20),
        ),
    ]