# Generated by Django 3.0.3 on 2020-06-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_repair'),
        ('repair', '0007_auto_20200611_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairorder',
            name='worker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='login.User', verbose_name='对应工人'),
        ),
    ]
