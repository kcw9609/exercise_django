# Generated by Django 4.1.1 on 2022-11-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingMall', '0006_post_delivery_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
