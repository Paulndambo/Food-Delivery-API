# Generated by Django 4.2.2 on 2023-06-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin'), ('customer_service', 'Customer Service'), ('restaurant', 'Restaurant')], default='individual', max_length=32),
        ),
    ]