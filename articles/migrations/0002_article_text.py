# Generated by Django 4.1.7 on 2023-04-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Article',
            name='text',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]
