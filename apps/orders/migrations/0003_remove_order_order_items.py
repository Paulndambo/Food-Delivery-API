# Generated by Django 4.2.2 on 2023-06-21 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cartitem_unique_together_remove_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
    ]
