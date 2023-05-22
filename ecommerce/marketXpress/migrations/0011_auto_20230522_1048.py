# Generated by Django 3.2.12 on 2023-05-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0010_alter_transaction_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_transaction',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]