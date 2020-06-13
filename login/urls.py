from django.urls import path, include

from . import views

urlpatterns =[
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/',views.index,name='index'),
    path('',views.ins,name='ins'),
    path('account/',views.account,name='account'),
    path('account/all_orders/',views.all_orders,name='all_orders'),
    path('account/repair_orders/',views.repair_orders,name='repair_orders'),
    path('account/account_subscribe/',views.account_subscribe,name='account_subscribe'),
]