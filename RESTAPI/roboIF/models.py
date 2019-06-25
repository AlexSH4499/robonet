#!/usr/bin/env python

from django.db import models
# from django.core.urlresolver import reverse
#https://medium.com/@jairvercosa/manger-vs-query-sets-in-django-e9af7ed744e0
# Create your models here.


# The Robot to use in facility
class Robot(models.Model):

    class Meta:
        ordering = ['uid']
    STATUS = (
        ('OFF','OFFLINE'),
        ('ON','ONLINE'),
        ('CAL','CALIBRATING'),
        ('ERR','ERROR')
    )

    # objects = RobotManager()
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS)
    # warehouse_id = models.ForeignKey(WareHouse, on_delete=models.CASCADE)#Physicial World Positioning
    location = models.CharField(max_length=30)
    # as_warehouse = factory_manager_for_warehouse(warehouse_id)

    def properties():
        return ('uid', 'name', 'status', 'location')
    # @property
    # def status(self):
    #     return self.status
    #
    # @property
    # def name(self):
    #     return self.name
    #
    # @property
    # def unique_id(self):
    #     return self.uid
    #
    # # @property
    # # def manager(self):
    # #     return self.robot_manager
    #
    # @property
    # def get_by_uid(self, id):
    #
    #     return self.manager().filter(uid=id)



    def filterable_props(self):#dict of all obj properties
        props = {k:v for k,v in self.__dict__ if k in properties()}
        return props

    # def get_absolute_url(self):
    #     return reverse('robot:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.uid} | {self.name} | {self.status}  | {self.location}'


class WareHouse(models.Model):
    class Meta:
        ordering = ['uid', 'name']

    #manager = models.Manager()

    uid = models.IntegerField(primary_key=True,default= 0)
    #objects = WareHouseManager(warehouse_id=uid)
    robots = models.ManyToManyField(Robot)
    name = models.CharField(max_length=30)

    def add_robot(self, robot):
        pass

    def remove_robot(self, robot):
        pass

    def __str__(self):

        return f'{self.name} | # Robots:{self.robots}'

class MovementRequest(models.Model):
    class Meta:
        ordering =['uid', 'robot_to_send']

    uid = models.IntegerField(primary_key=True)
    robot_to_send = models.ForeignKey(Robot, on_delete=models.CASCADE)

    joint_1 = models.DecimalField(max_digits=6, decimal_places=2)
    joint_2 = models.DecimalField(max_digits=6, decimal_places=2)
    joint_3 = models.DecimalField(max_digits=6, decimal_places=2)

    joint_4 = models.DecimalField(max_digits=6, decimal_places=2)
    joint_5 = models.DecimalField(max_digits=6, decimal_places=2)
    joint_6 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Request [{self.uid}] | target: {self.robot_to_send.name}'




#
# class WareHouseManager(models.Manager):
#     def __init__(self, warehouse_id=None, *args, **kwargs):
#         self._warehouse_id = warehouse_id
#         super().__init__(*args, **kwargs)
#         return
#
#     def find(self, warehouse_id):
#         queryset = self.get_queryset()
#
#         try:
#             instance = queryset.get(pk=warehouse_id)
#         except ObjectDoesNotExist:
#             instance = None
#
#         finally:
#             return instance
#
#     def find_all_robots(self, warehouse_id :int):
#         queryset = self.get_queryset()
#         return queryset.filter(warehouse_id=warehouse_id)
#
#     def factory_manager_for_warehouse(warehouse_id):
#         return RobotManager.factory(r)










#
# class RobotQuerySet(models.QuerySet):
#
#     def  some_filter(self):
#         return (
#             self.annotate(
#                 count_category=Count(
#                     'a__category__idk'
#                 )
#             )
#             .filter(count_category_gt=1)
#         )
#
#
#
# def factory_manager_for_warehouse(warehouse_id):
#     return RobotManager.factory(model=Robot, warehouse_id=warehouse_id)
#
# from typing import Optional
#
# class RobotManager(models.Manager):
#
#     def __init__(self, warehouse_id=None, *args, **kwargs):
#         self._warehouse_id = warehouse_id
#         super().__init__(*args, **kwargs)
#
#
#     def __str__(self):
#
#         return
#
#     def get_queryset(self):
#         queryset = RobotQuerySet(
#             model = self.model,
#             using = self._db,
#             hints=self._hints
#         )
#
#         if self._warehouse_id is not None:
#             queryset = queryset.filter(warehouse_id=self._warehouse_id)
#
#         return queryset
#
#
#
#     @classmethod
#     def factory(cls, model, warehouse_id=None):
#         manager=cls(warehouse_id)
#         manager.model = model
#         return manager
#
#     def find(self, robot_id):
#         queryset = self.get_queryset()
#
#         try:
#             instance = queryset.get(pk=robot_id)
#         except ObjectDoesNotExist:
#             instance = None
#
#         finally:
#             return instance
#
#     def find_all_with_warehouse(self, warehouse_id :int):
#         queryset = self.get_queryset()
#         return queryset.filter(location=warehouse_id)
