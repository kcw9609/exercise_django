# Generated by Django 4.1.1 on 2022-11-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingMall', '0005_remove_post_address_remove_post_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='delivery_charge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
