# Generated by Django 4.1.7 on 2023-04-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
