# Generated by Django 3.1.1 on 2020-09-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_auto_20200924_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_rating',
            name='star',
            field=models.IntegerField(null=True),
        ),
    ]
