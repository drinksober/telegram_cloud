# Generated by Django 2.0.5 on 2018-06-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_account_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='facebook',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='account',
            name='twitter',
            field=models.CharField(default='', max_length=15),
        ),
    ]