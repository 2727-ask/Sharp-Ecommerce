# Generated by Django 3.1.1 on 2020-09-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_product_rating_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_rating',
            name='star',
            field=models.IntegerField(default=1),
        ),
    ]
