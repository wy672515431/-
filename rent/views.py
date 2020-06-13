import hashlib
import json
import datetime
import calendar

from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.urls import reverse
from rent.models import rentOrder
from . import forms
from house.models import house
from login.models import  User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import FileResponse


def search(request):
    if request.method == "GET":
        houses = request.session.get('houses',None)
        house_list = house.objects.all()
        flag = 1
        if houses:
            for i in houses:
                print(i)
                print(flag)
                if i != 0:
                    if flag == 1:
                        if i == 1:
                            pass
                        elif i == 2:
                            house_list = house_list.filter(area='ChaoYang')
                        elif i == 3:
                            house_list = house_list.filter(area='HaiDian')
                        elif i == 4:
                            house_list = house_list.filter(area='ChangPing')
                    elif flag == 2:
                        if i == 1:
                            house_list = house_list.filter(rental__lte=1000)
                        elif i == 2:
                            house_list = house_list.filter(rental__gt=1000, rental__lte=1500)
                        elif i == 3:
                            house_list = house_list.filter(rental__gt=1500, rental__lte=2000)
                        elif i == 4:
                            house_list = house_list.filter(rental__gt=2000, rental__lte=3000)
                        elif i == 5:
                            house_list = house_list.filter(rental__gt=3000)
                    elif flag == 3:
                        if i == 1:
                            house_list = house_list.filter(type='single')
                        elif i == 2:
                            house_list = house_list.filter(type='double')
                        elif i == 3:
                            house_list = house_list.filter(type='triple')
                        elif i == 4:
                            house_list = house_list.filter(type='quad')
                    elif flag == 4:
                        if i == 1:
                            house_list = house_list.filter(elevator=True)
                        elif i == 2:
                            house_list = house_list.filter(elevator=False)
                elif i == 0:
                    flag += 1
                if flag == 6:
                    keyword = request.session.get('keyword', None)
                    print(keyword)
                    if keyword:
                        house_list = house.objects.filter(housename__contains=keyword)



    if request.method == "POST":
        house_list = house.objects.all()
        houses = []
        if 'area' in request.POST:
            areas = request.POST.getlist('area',[])
            print('areas')
            for i in range(0,len(areas)):
                print (areas[i])
                if areas[i] == '1':
                    houses.append(1)
                elif areas[i] == '2':
                    houses.append(2)
                    house_list = house_list.filter(area='ChaoYang')
                elif areas[i] == '3':
                    houses.append(3)
                    house_list = house_list.filter(area='HaiDian')
                elif areas[i] == '4':
                    houses.append(4)
                    house_list = house_list.filter(area='ChangPing')
        houses.append(0)
        if 'rental' in request.POST:
            rentals = request.POST.getlist('rental',[])
            print('rentals')
            for i in range(0,len(rentals)):
                print(rentals[i])
                if rentals[i] == '1':
                    houses.append(1)
                    house_list = house_list.filter(rental__lte=1000)
                elif rentals[i] == '2':
                    houses.append(2)
                    house_list = house_list.filter(rental__gt=1000,rental__lte=1500)
                elif rentals[i] == '3':
                    houses.append(3)
                    house_list = house_list.filter(rental__gt=1500, rental__lte=2000)
                elif rentals[i] == '4':
                    houses.append(4)
                    house_list = house_list.filter(rental__gt=2000,rental__lte=3000)
                elif rentals[i] == '5':
                    houses.append(5)
                    house_list = house_list.filter(rental__gt=3000)
        houses.append(0)
        if 'type' in request.POST:
            types = request.POST.getlist('type',[])
            print('types')
            for i in range(0,len(types)):
                print(types[i])
                if types[i] == '1':
                    houses.append(1)
                    house_list = house_list.filter(type='single')
                elif types[i] == '2':
                    houses.append(2)
                    house_list = house_list.filter(type='double')
                elif types[i] == '3':
                    houses.append(3)
                    house_list = house_list.filter(type='triple')
                elif types[i] == '4':
                    houses.append(4)
                    house_list = house_list.filter(type='quad')
        houses.append(0)
        if 'elevator' in request.POST:
            elevators = request.POST.getlist('elevator', [])
            print('elevators')
            for i in range(0, len(elevators)):
                print(elevators[i])
                if elevators[i] == '1':
                    houses.append(1)
                    house_list = house_list.filter(elevator=True)
                elif elevators[i] == '2':
                    houses.append(2)
                    house_list = house_list.filter(elevator=False)
        houses.append(0)
        if 'keyword' in request.POST:
            keyword = request.POST.get('keyword')
            print('keyword')
            house_list = house.objects.filter(housename__contains=keyword)
            request.session['keyword'] = keyword
            houses.append(0)
        request.session['houses'] = houses

    house_list = house_list.order_by('id')
    paginator = Paginator(house_list,2)
    try:
        page_num = request.GET.get('page',1)
        page = paginator.page(page_num)
    except PageNotAnInteger as e:
        # 不是整数返回第一页数据
        page = paginator.page('1')
        page_num = 1
    except EmptyPage as e:
        # 当参数页码大于或小于页码范围时,会触发该异常
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # 大于 获取最后一页数据返回
            page = paginator.page(paginator.num_pages)
        else:
            # 小于 获取第一页
            page = paginator.page(1)

        # 这部分是为了再有大量数据时，仍然保证所显示的页码数量不超过10，
    page_num = int(page_num)
    if page_num < 6:
        if paginator.num_pages <= 10:
            pageRange = range(1, paginator.num_pages + 1)
        else:
            pageRange = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        pageRange = range(page_num - 5, page_num + 5)
    else:
        pageRange = range(paginator.num_pages - 9, paginator.num_pages + 1)


    return render(request,'rent/search.html',locals())

@csrf_exempt
def pay(request,rentorder_id):
    order = rentOrder.objects.get(id=rentorder_id)
    return render(request, 'rent/pay.html', locals())
#TODO:长租的pay应该提示下载合同，审核问题


def download_template(request):
    file = open('static/files/hetong.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="hetong.docx"'
    return response
