# Generated by Django 2.0.5 on 2018-05-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180527_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='twitter',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
