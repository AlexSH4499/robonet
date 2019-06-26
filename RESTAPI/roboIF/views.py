#!/usr/bin/env python

from django.views.generic.edit import CreateView, UpdateView,DeleteView
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
# class RobotList(APIView):

    # def get(self, request):
    #     robs = Robot.objects.all()
    #     #serializer = RobotSerializer(robs, many=True)
    #     serializer = RobotSerializer
    #     return Response(serializer.data)

# / robots
class RobotView(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    @action(methods=['put'], detail=True)#@action(methods=['put'], detail=True, permission_classes=[IsAdminOrIsSelf]
    def set_status(self,request, pk=None):
        if pk is None:
            msg ="Error Invalid private key"
            return HtttpResponse(msg, status_code=404)

        robot = queryset.filter(pk)



    #permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

#/warehouses
class WareHouseView(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    #permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

#requests
class RequestsView(viewsets.ModelViewSet):

    queryset = MovementRequest.objects.all()
    serializer_class = RequestSerializer#many is when we want to store a bunch at once

    @action(methods=['post'], detail=True)
    def post(self,request):
        form = MovementRequestForm(request.POST)

        if form.is_valid():
            form.save()
            text = form.cleaned_data['post']
    # @action(detail=True, methods=['post'])
    # def create_request(self, request, pk=None):
    #
    #     return
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk):
        if pk is None:
            queryset = MovementRequest.objects.all()
            serializer = RequestSerializer(queryset, many=True)
            return Response(serializer.data)

        queryset = MovementRequest.objects.all()
        rq = get_object_or_404(queryset,pk=pk)
        serializer = RequestSerializer(rq)

        return Response(serializer.data)

class RequestsCreate(viewsets.ModelViewSet):
    model = MovementRequest
    fields = ['uid', 'robot_to_send','joint_1',
                'joint_2','joint_3','joint_4',
                'joint_5','joint_6']

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
