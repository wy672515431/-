import hashlib
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.urls import reverse
from login.models import User
from rent.models import rentOrder
from house.models import house
from . import forms
from repair.models import repairOrder,subscribe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def repair(request):
    message = request.session.get('username')
    message2 =""
    if request.method=="POST":
        try:
            rentorder = rentOrder.objects.get(id=request.POST.get('repairid'))

            Repair = repairOrder()
            Repair.rentorder = rentorder

            repair_ownUser = rentorder.rent_ownUser
            Repair.repair_ownUser = repair_ownUser

            House = rentorder.house
            Repair.house = House

            content = request.POST.get('information')
            Repair.content = content

            Repair.worker = User.objects.get(username='dc')

            response = "未回复"
            Repair.response = response

            Repair.repair_paidUser = User.objects.get(username=message)
            Repair.save()
        except ObjectDoesNotExist:
            message2 = "订单号不存在，请重新输入"
            return render(request, 'repair/repair.html', locals())

    return render(request,'repair/repair.html',locals())

def subscribepost(request):
    message = request.session.get('username')
    if request.method == "POST":
        Subscribe = subscribe()

        owner = User.objects.get(username=request.session.get('username'))
        Subscribe.owner = owner

        content = request.POST.get('information')
        Subscribe.content = content

        response = "未回复"
        Subscribe.response=response

        Subscribe.save()
    return render(request,'repair/subscribe.html',locals())