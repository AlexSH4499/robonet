#!/usr/bin/env python

from rest_framework import serializers
from roboIF.models import Robot, WareHouse, MovementRequest

class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('uid', 'name','status', 'location')

class WareHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WareHouse
        fields = ('uid','name','robots')

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovementRequest
        fields = ('uid','robot_to_send',
                    'joint_1','joint_2','joint_3',
                    'joint_4','joint_5','joint_6')
