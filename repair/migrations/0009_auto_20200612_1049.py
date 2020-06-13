# Generated by Django 3.0.3 on 2020-06-12 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20200609_1547'),
        ('login', '0003_user_repair'),
        ('repair', '0008_repairorder_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairorder',
            name='response',
            field=models.CharField(default=None, max_length=256, verbose_name='回复内容'),
        ),
        migrations.AlterField(
            model_name='repairorder',
            name='content',
            field=models.CharField(default=None, max_length=256, verbose_name='报修内容'),
        ),
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default=None, max_length=256, verbose_name='投诉内容')),
                ('response', models.CharField(default=None, max_length=256, verbose_name='回复内容')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='login.User', verbose_name='投诉者')),
                ('rentorder_s', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rentorder_s', to='rent.rentOrder', verbose_name='对应订单')),
            ],
        ),
    ]