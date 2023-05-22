# Generated by Django 3.2.12 on 2023-05-22 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketXpress', '0003_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_product',
            field=models.ManyToManyField(to='marketXpress.Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_brand',
            field=models.ManyToManyField(to='marketXpress.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketXpress.brand'),
        ),
    ]