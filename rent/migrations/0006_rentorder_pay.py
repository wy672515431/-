# Generated by Django 3.0.3 on 2020-06-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20200609_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentorder',
            name='pay',
            field=models.BooleanField(default=False, verbose_name='付款结果'),
        ),
    ]