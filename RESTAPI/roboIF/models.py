from django.db import models

# Create your models here.
# The Robot to use in facility
class Robot(models.Model):
    as_warehouse = factory_manager_for_warehouse
    class Meta:
        ordering = ['uid']
    STATUS = (
        ('OFF','OFFLINE'),
        ('ON','ONLINE'),
        ('CAL','CALIBRATING'),
        ('ERR','ERROR')
    )

    objects = RobotManager()
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS)
    warehouse_id = models.ForeignKey(WareHouse, on_delete=models.CASCADE)#Physicial World Positioning

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

    def create_robot(id, name, stat, loc):
        return Robot(uid=id, name=name, status=stat, warehouse_id=loc)

    def filterable_props(self):#dict of all obj properties
        props = {k:v for k,v in self.__dict__ if k in properties()}
        return props

    def __str__(self):
        return f'{self.uid} | {self.name} | {self.status}  | {self.warehouse_id}'

class WareHouse(models.Model):
    class Meta:
        ordering = ['uid', 'name']

    #manager = models.Manager()
    objects = WareHouseManager()
    uid = models.IntegerField(primary_key=True)
    robots = models.ManyToManyField(Robot)
    name = models.CharField(max_length=30)

    def add_robot(self, robot):
        pass

    def remove_robot(self, robot):
        pass


from typing import Optional
class RobotManager(models.Manager):

    def __init__(self, warehouse_id=None, *args, **kwargs):
        self._warehouse_id = warehouse_id
        super().__init__(*args, **kwargs)


    def __str__(self):

        return

    def get_queryset(self)-> RobotQuerySet:
        queryset = RobotQuerySet(
            model = self.model,
            using = self._db,
            hints=self._hints
        )

        if self._warehouse_id is not None:
            queryset = queryset.filter(warehouse_id=self._warehouse_id)

        return queryset

    @classmethod
    def factory(cls, model, warehouse_id=None):
        manager=cls(warehouse_id)
        manager.model = model
        return manager

    def find(self, robot_id:int) -> Optional['Robot']:
        queryset = self.get_queryset()

        try:
            instance = queryset.get(pk=robot_id)
        except ObjectDoesNotExist:
            instance = None

        finally:
            return instance

    def find_all_with_warehouse(self, warehouse_id :int) -> QuerySet:
        queryset = self.get_queryset()
        return queryset.filter(location=warehouse_id)



class WareHouseManager(models.Manager):

    def find(self, warehouse_id:int) -> Optional['WareHouse']:
        queryset = self.get_queryset()

        try:
            instance = queryset.get(pk=warehouse_id)
        except ObjectDoesNotExist:
            instance = None

        finally:
            return instance

    def find_all_robots(self, warehouse_id :int) -> QuerySet:
        queryset = self.get_queryset()
        return queryset.filter(warehouse_id=warehouse_id)
