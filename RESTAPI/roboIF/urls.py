#!/usr/bin/env python

from django.urls import path, include
#from views import RobotList, RobotView
from roboIF import views
from rest_framework import routers
from rest_framework.urlpatterns import  format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'robots', views.RobotView)
router.register(r'warehouses', views.WareHouseView)
router.register(r'requests',views.RequestsView)
# router.register(r'robots/add/$',views.RequestsCreate)

urlpatterns = [
    #path(r'/robots', RobotList.as_view()),
    path('schema/',schema_view),
    path('', include(router.urls))
]
