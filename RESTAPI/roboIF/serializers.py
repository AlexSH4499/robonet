from rest_framework import serializers
from roboIF.models import Robot, WareHouse

class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('uid', 'name','status', 'location')

class WareHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WareHouse
        fields = ('uid','name','robots')
