# Generated by Django 4.1.7 on 2023-04-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Article',
            name='text',
            field=models.TextField(),
        ),
    ]
