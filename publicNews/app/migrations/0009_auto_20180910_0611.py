# Generated by Django 2.0.7 on 2018-09-10 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180904_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstype',
            name='newspublic',
        ),
        migrations.DeleteModel(
            name='NewsType',
        ),
    ]
