# Generated by Django 3.1 on 2021-11-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20211124_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
