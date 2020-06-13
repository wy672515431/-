from django.urls import path, include
from . import views

urlpatterns=[
    path('search/',views.search,name='search'),
    path('pay/<int:rentorder_id>',views.pay,name='pay'),
    path('download/', views.download_template)
]