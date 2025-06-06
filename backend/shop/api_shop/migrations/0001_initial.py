# Generated by Django 5.2.1 on 2025-05-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discount Price')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock Quantity')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Brand')),
                ('category', models.CharField(choices=[('kitchen', 'Kitchen Appliances'), ('cleaning', 'Cleaning Appliances'), ('entertainment', 'Entertainment Devices'), ('climate', 'Heating/Cooling'), ('other', 'Other')], max_length=50, verbose_name='Category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Product Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
