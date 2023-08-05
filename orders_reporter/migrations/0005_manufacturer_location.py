# Generated by Django 3.2.18 on 2023-04-20 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders_reporter', '0004_rename_name_manufacturer_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]