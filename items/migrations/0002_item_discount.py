# Generated by Django 4.2.13 on 2024-05-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Discount'),
        ),
    ]
