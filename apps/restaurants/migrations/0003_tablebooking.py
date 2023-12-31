# Generated by Django 4.2.2 on 2023-06-20 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0002_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('booked_from', models.DateTimeField()),
                ('booked_up_to', models.DateTimeField()),
                ('booking_status', models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled'), ('fullfilled', 'Full Filled')], default='active', max_length=255)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.restauranttable')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
