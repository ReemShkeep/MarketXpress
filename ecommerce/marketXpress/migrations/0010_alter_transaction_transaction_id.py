# Generated by Django 3.2.12 on 2023-05-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0009_auto_20230522_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]