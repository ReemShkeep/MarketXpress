# Generated by Django 3.2.12 on 2023-05-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0006_auto_20230522_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_order_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
