# Generated by Django 3.0.5 on 2020-08-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200813_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ad_say',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
