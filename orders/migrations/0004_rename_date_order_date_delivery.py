# Generated by Django 4.1.7 on 2023-02-27 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='date_delivery',
        ),
    ]
