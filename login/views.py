import hashlib
import datetime
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.urls import reverse
from . import models as login_models
from rent.models import rentOrder
from repair.models import repairOrder,subscribe
from . import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def ins(request):
    return redirect(reverse('login'))

def login(request):
    login_form = forms.UserForm()
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            try:
                username = login_form.cleaned_data['username']
            except:
                message = "账号无效"
                return render(request, 'login/login.html', locals())
            password = login_form.cleaned_data['password']
            try:
                user = login_models.User.objects.get(username=username)
                if user.password == password:
                    try:
                        request.session['is_login'] = True
                        request.session['username'] = user.username # 之后可以通过session的username查询获取user的information
                        return redirect(reverse('index'))
                    except:
                        message="session wrong"
                else:
                    message = "密码错误"
            except:
                message = "用户不存在"
    return render(request,'login/login.html',locals())

def register(request):
    register_form = forms.RegisterForm()
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = "两次输入密码不同"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = login_models.User.objects.filter(username=username)
                if same_name_user:
                    message = "用户已经存在，请重新选择用户名"
                    return render(request, 'login/register.html', locals())
                same_email_user = login_models.User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱地址已被注册，请使用别的邮箱"
                    return render(request, 'login/register.html', locals())

                # everything ok,then creat new account

                new_user = login_models.User()
                new_user.username = username
                new_user.password = password1
                new_user.email = email
                new_user.save()
                return redirect(reverse('login'))
    return render(request, 'login/register.html', locals())

def index(request):
    message = request.session.get("username",None)
    if message:
        return render(request,'login/index1.html',locals())
    else:
        return render(request,'login/index.html',locals())

def account(request):
    user = login_models.User.objects.get(username=request.session.get('username'))
    print(user.username)
    print(user.email)
    return render(request,'login/account.html',locals())

def re_account(request):
    return render(request,'login/reaccount.html',locals())

def all_orders(request):
    orders = rentOrder.objects.filter(Q(rent_ownUser = request.session.get('username')) | Q(rent_paidUser = request.session.get('username')))

    paginator = Paginator(orders, 2)
    try:
        page_num = request.GET.get('page', 1)
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
    return render(request,'login/all_orders.html',locals())

def repair_orders(request):
    re_orders = repairOrder.objects.filter(
        Q(repair_ownUser=request.session.get('username')) | Q(repair_paidUser=request.session.get('username')))
    paginator = Paginator(re_orders, 4)
    try:
        page_num = request.GET.get('page', 1)
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
    return render(request,'login/repair_orders.html',locals())

def account_subscribe(request):
    subscribes = subscribe.objects.filter(
        owner=request.session.get('username'))
    paginator = Paginator(subscribes, 4)
    try:
        page_num = request.GET.get('page', 1)
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
    return render(request,'login/account_subscribe.html',locals())
