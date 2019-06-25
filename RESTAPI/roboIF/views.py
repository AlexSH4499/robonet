#!/usr/bin/env python


from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from roboIF.serializers import *
from roboIF.models import Robot, WareHouse

#/robots
class RobotList(APIView):

    def get(self, request):
        robs = Robot.objects.all()
        #serializer = RobotSerializer(robs, many=True)
        serializer = RobotSerializer
        return Response(serializer.data)

class RobotView(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    #
    @action(methods=['put'], detail=True)#@action(methods=['put'], detail=True, permission_classes=[IsAdminOrIsSelf]
    def set_status(self,request, pk=None):
        if pk is None:
            msg ="Error Invalid private key"
            return HtttpResponse(msg, status_code=404)

        robot = queryset.filter
    #permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

class WareHouseView(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    #permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

class RequestsView(viewsets.ModelViewSet):

    queryset = MovementRequest.objects.all()
    serializer_class = RequestSerializer

def list_models(model, uid):
    try:
        return model.objects.get(uid=uid)
    except ObjectDoesNotExist:
        msq = f'There exist no objects of {uid}'
        raise ObjectDoesNotExist(msg)

# Create your views here.
def index(request):
    print(request.headers)

    return render(request, 'debugging/index.html', {'headers':request.headers})
    # if request.method == 'GET':
    #     #get_object_or404()
    #     pass
    #
    # if request.method == 'POST':
    #     pass
    #
    # if request.method == 'DELETE':
    #     pass
    #
    # if request.method == 'PUT':
    #     pass
    #
    # else:
    #     #raise Error()
    #     pass
