# Generated by Django 3.1.1 on 2020-09-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20200923_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img_4',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
