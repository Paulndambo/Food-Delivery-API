# Generated by Django 4.2.2 on 2023-06-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.JSONField(null=True),
        ),
    ]
