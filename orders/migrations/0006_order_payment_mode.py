# Generated by Django 3.1 on 2021-11-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
