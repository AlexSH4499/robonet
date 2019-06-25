#!/usr/bin/env python

from django.contrib import admin

from .models import Robot, WareHouse, MovementRequest


# Register your models here.
admin.site.register(Robot)
admin.site.register(WareHouse)
admin.site.register(MovementRequest)
