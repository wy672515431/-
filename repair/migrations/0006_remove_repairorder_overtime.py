# Generated by Django 3.0.3 on 2020-06-11 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0005_auto_20200611_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairorder',
            name='overtime',
        ),
    ]