# Generated by Django 4.0.5 on 2022-06-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_alter_product_miniimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='miniimage',
            field=models.ImageField(default='', upload_to='ecom/'),
        ),
    ]
