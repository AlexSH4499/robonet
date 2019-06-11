from django.db import models

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

    robot_manager = models.Manager()

    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS)
    location = models.CharField()#Physicial World Positioning

    @property
    def status(self):
        return self.status

    @property
    def name(self):
        return self.name

    @property
    def unique_id(self):
        return self.uid

    @property
    def manager(self):
        return self.robot_manager

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
