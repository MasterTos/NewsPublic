# Generated by Django 2.0.7 on 2018-09-10 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180910_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspublic',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
