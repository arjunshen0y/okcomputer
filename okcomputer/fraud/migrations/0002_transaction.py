# Generated by Django 3.1.3 on 2020-12-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=264)),
                ('old_balance_org', models.CharField(max_length=264)),
                ('new_balance_org', models.CharField(max_length=264)),
                ('old_balance_dest', models.CharField(max_length=264)),
                ('new_balance_dest', models.CharField(max_length=264)),
                ('cat', models.CharField(choices=[('cashout', 'CASH OUT'), ('payment', 'PAYMENT'), ('cashin', 'CASHIN'), ('transfer', 'TRANSFER'), ('debit', 'DEBIT')], default='cashout', max_length=264)),
            ],
        ),
    ]
