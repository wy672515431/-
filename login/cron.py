import datetime

from django.core.mail import send_mail
from rent.models import rentOrder
from login.models import User

def test():
    orders = rentOrder.objects.filter(type='long')
    for order in orders:
        user = order.rent_paidUser
        send_mail('房租缴费提醒', "您的订单:" + str(order.id) + "本月房租未交，请前往缴费", '1205672770@qq.com', [user.email])
