# Generated by Django 2.2 on 2019-04-29 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0005_auto_20190429_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='builditem',
            old_name='stock',
            new_name='stock_item',
        ),
    ]