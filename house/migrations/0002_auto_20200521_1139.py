# Generated by Django 3.0.3 on 2020-05-21 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200423_1619'),
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourse',
            name='User',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
