# Generated by Django 3.2.12 on 2023-05-23 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Brand Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Category Name')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Customer Name')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('age', models.PositiveIntegerField(default=18)),
                ('email', models.CharField(max_length=200, null=True)),
                ('shippingAddress', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Product Price')),
                ('instock', models.BooleanField(blank=True, default=True, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketXpress.brand')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketXpress.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('customer_order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketXpress.customer')),
                ('order_product', models.ManyToManyField(to='marketXpress.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_product',
            field=models.ManyToManyField(to='marketXpress.Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketXpress.category'),
        ),
    ]
