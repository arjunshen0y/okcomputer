
# Generated by Django 3.1.3 on 2020-12-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0003_auto_20201215_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transfer_type',
            field=models.CharField(choices=[('cashout', 'CASH OUT'), ('payment', 'PAYMENT'), ('cashin', 'CASH IN'), ('transfer', 'TRANSFER'), ('debit', 'DEBIT')], default='cashout', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='cat',
            field=models.IntegerField(default=0),
        ),
    ]

