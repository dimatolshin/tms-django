# Generated by Django 4.1.7 on 2023-06-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
