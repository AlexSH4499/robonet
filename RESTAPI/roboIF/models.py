from django.db import models

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

    #robot_manager = models.Manager()

    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS)
    location = models.CharField(max_length=15)#Physicial World Positioning

    # def properties():
    #     return ('uid', 'name', 'status', 'location')
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
        return Robot(uid=id, name=name, status=stat, location=loc)

    def filterable_props(self):#dict of all obj properties
        props = {k:v for k,v in self.__dict__ if k in properties()}
        return props

    def __str__(self):
        return f'{self.uid} | {self.name} | {self.status}  | {self.location}'

class WareHouse(models.Model):
    class Meta:
        ordering = ['uid', 'name']

    manager = models.Manager()
    uid = models.IntegerField(primary_key=True)
    robots = models.ManyToManyField(Robot)
    name = models.CharField(max_length=30)

    def add_robot(self, robot):
        pass

    def remove_robot(self, robot):
        pass
