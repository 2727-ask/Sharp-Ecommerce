# Generated by Django 3.1.1 on 2020-09-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_product_rating_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_desc1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_desc2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_head1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_head2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_img1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_img2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_6',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_7',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_8',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_keyf_9',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price_starting',
        ),
        migrations.AddField(
            model_name='product',
            name='brand_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='product_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]