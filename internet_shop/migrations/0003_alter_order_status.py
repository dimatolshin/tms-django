# Generated by Django 4.1.7 on 2023-05-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0002_order_product_price_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('INITIAL', 'Initial'), ('COMPLETED', 'Completed'), ('DELIVERED', 'Delivered')], default='INITIAL', max_length=20),
        ),
    ]
