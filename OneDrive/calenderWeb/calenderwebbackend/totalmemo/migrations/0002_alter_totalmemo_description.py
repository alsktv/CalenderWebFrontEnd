# Generated by Django 5.0.6 on 2024-06-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totalmemo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalmemo',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
    ]
