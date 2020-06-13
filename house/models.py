from django.db import models

class house(models.Model):
    type=(
        ("single","单人间"),
        ("double","双人间"),
        ("triple","三人间"),
        ("quad","四人间")
    )
    orientation=(
        ("north","北"),
        ("east","东"),
        ("west","西"),
        ("south","南")
    )
    area=(
        ("ChaoYang","朝阳区"),
        ("HaiDian","海淀区"),
        ("ChangPing","昌平区"),
        ("Unknown","未知")
    )
    housename = models.CharField(max_length=32)
    space = models.DecimalField(max_digits=6,decimal_places=2)
    area = models.CharField(verbose_name="区域",max_length=32,choices=area,default="Unknown")
    location = models.CharField(max_length=64)
    type = models.CharField(max_length=32,choices=type)
    orientation = models.CharField(verbose_name="朝向",max_length=32,choices=orientation)
    rental = models.IntegerField(verbose_name="租金")
    elevator = models.BooleanField()
    introduction = models.CharField(verbose_name="简介",max_length=256,default="暂无简介")
    image = models.CharField(verbose_name="图片路径",max_length=64,default="img/house/")

    User = models.ForeignKey("login.User",on_delete=models.CASCADE,default=None)


