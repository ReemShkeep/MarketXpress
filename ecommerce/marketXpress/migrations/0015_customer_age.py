# Generated by Django 3.2.12 on 2023-05-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0014_remove_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]