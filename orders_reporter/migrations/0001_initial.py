# Generated by Django 4.1.4 on 2023-01-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('store_sku', models.CharField(max_length=100)),
                ('omsid', models.CharField(max_length=100)),
                ('store_so_sku', models.CharField(max_length=100)),
                ('parts_usage', models.CharField(max_length=100)),
            ],
        ),
    ]
