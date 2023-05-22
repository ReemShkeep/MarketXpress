# Generated by Django 3.2.12 on 2023-05-22 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0008_alter_customer_customer_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='order',
            name='order_transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketXpress.transaction'),
        ),
    ]
