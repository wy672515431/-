from django.urls import path, include
from . import views

urlpatterns=[
    path('repair/',views.repair,name='repair'),
    path('subscribe/',views.subscribepost,name='subscribe'),
]