# Generated by Django 4.2.2 on 2023-06-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
