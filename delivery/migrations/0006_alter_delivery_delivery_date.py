# Generated by Django 4.2.3 on 2023-08-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_alter_delivery_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]
