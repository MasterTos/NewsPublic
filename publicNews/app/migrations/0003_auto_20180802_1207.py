# Generated by Django 2.0.6 on 2018-08-02 05:07

import app.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180801_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspublic',
            name='content',
            field=app.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
