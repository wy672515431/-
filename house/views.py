import hashlib
import datetime
import calendar

from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.urls import reverse
from house.models import house
from login.models import  User
from . import forms
from rent.models import rentOrder

def house_detail(request,house_id):
    if request.method=="POST":
        order = rentOrder()

        order.id = len(rentOrder.objects.all())+1

        date = datetime.datetime.strptime(request.POST.get('begin'),"%Y-%m-%d")
        order.begintime = date

        House = house.objects.get(id=house_id)
        order.house = House
        order.rent_ownUser = House.User
        user = User.objects.get(username=request.session.get('username'))
        order.rent_paidUser = user

        money = 0;
        if request.POST.get('numOfDay'):
            money =  House.rental * int(request.POST.get('numOfDay'))
            date = (date + datetime.timedelta(days=int(request.POST.get('numOfDay'))))
        elif request.POST.get('numOfMon'):
            money = House.rental * int(request.POST.get('numOfMon')) * 30
            months = int(request.POST.get('numOfMon'))
            month = date.month - 1 + months
            year = int(date.year + month / 12)
            month = int(month % 12 + 1)
            day = min(date.day, calendar.monthrange(year, month)[1])
            date = date.replace(year=year,month=month,day=day)
        order.overtime = date
        if request.POST.get('orderType')=='1':
            order.type = "long"
        elif request.POST.get('orderType')=='2':
            order.tpye="short"

        order.money = money

        order.save()
    House = house.objects.get(id=house_id)
    return render(request,'house/house.html',locals())