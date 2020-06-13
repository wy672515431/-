# Generated by Django 3.0.3 on 2020-05-27 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20200521_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=32)),
                ('space', models.DecimalField(decimal_places=2, max_digits=6)),
                ('area', models.CharField(choices=[('ChaoYang', '朝阳区'), ('HaiDian', '海淀区'), ('ChangPing', '昌平区'), ('Unknown', '未知')], default='Unknown', max_length=32, verbose_name='区域')),
                ('location', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('single', '单人间'), ('double', '双人间'), ('triple', '三人间'), ('quad', '四人间')], max_length=32)),
                ('orientation', models.CharField(choices=[('north', '北'), ('east', '东'), ('west', '西'), ('south', '南')], max_length=32, verbose_name='朝向')),
                ('rental', models.IntegerField(verbose_name='租金')),
                ('elevator', models.BooleanField()),
                ('introduction', models.CharField(default='暂无简介', max_length=256, verbose_name='简介')),
            ],
        ),
        migrations.RemoveField(
            model_name='hourse',
            name='User',
        ),
    ]