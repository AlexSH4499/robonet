

from django.urls import path, include
from roboIF.views import RobotList

urlpatterns = [
    path(r'^robots/', RobotList.as_view()),

]
