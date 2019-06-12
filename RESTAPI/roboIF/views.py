
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import RobotSerializer
from .models import Robot

#/robots
class RobotList(APIView):

    def get(self, request):
        robs = Robot.robot_manager.all()
        serializer = RobotSerializer(robs, many=True)
        return Response(serializer.data)

class RobotView(viewsets.ModelViewSet):
    queryset = Robot.manager().all()
    serializer_cls = RobotSerializer()


def list_models(model, uid):
    try:
        return model.objects.get(uid=uid)
    except ObjectDoesNotExist:
        msq = f'There exist no objects of {uid}'
        raise ObjectDoesNotExist(msg)

# Create your views here.
def index(request):

    if request.method == 'GET':
        #get_object_or404()
        pass

    if request.method == 'POST':
        pass

    if request.method == 'DELETE':
        pass

    if request.method == 'PUT':
        pass

    else:
        #raise Error()
        pass
