# Generated by Django 3.1.13 on 2023-08-04 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_reporter', '0011_rename_note_note_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
