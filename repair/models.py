from django.db import models

class repairOrder(models.Model):
    begintime = models.DateField(auto_now_add=True, verbose_name="开始时间")
    state = models.BooleanField(verbose_name="完成结果",default=False)
    worker = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='worker',verbose_name="对应工人",default=None)
    rentorder = models.ForeignKey("rent.rentOrder",on_delete=models.CASCADE,related_name='rentorder',verbose_name="对应订单",default=None)
    repair_ownUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_ownUser',verbose_name="房东",default=None)
    repair_paidUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_paidUser',verbose_name="房客",default=None)
    house = models.ForeignKey("house.house",on_delete=models.CASCADE,default=None)
    content = models.CharField(verbose_name="报修内容",max_length=256,default=None)
    response = models.CharField(verbose_name="回复内容", max_length=256,default=None)

class subscribe(models.Model):
    owner = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='owner',verbose_name="投诉者",default=None)
    content = models.CharField(verbose_name="投诉内容", max_length=256,default=None)
    response = models.CharField(verbose_name="回复内容", max_length=256,default=None)