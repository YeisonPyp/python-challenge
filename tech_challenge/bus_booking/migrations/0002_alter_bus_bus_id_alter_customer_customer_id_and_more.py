# Generated by Django 4.0 on 2023-11-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='traveldetail',
            name='travel_detail_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
