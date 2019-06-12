
from django.urls import path, include
# from views import RobotList, RobotView
from roboIF import views
from rest_framework import routers
from rest_framework.urlpatterns import  format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'robots', views.RobotView)

urlpatterns = [
    #path(r'/robots', RobotList.as_view()),
    path('', include(router.urls))
]
