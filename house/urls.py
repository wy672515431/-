from django.urls import path, include
from . import views

app_name = 'house'
urlpatterns=[
    path('house/<int:house_id>/',views.house_detail,name='house'),
]