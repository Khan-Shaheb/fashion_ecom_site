# Generated by Django 3.1 on 2020-09-16 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_shopcart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
