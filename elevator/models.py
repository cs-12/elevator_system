from django.db import models

# Create your models here.  

class Elevator(models.Model):
    """
    Represents an elevator in a building.

    Attributes:
        id (AutoField): The primary key of the elevator.
        location (str): The location of the elevator.
        status (ForeignKey): The current status of the elevator.
        current_floor (int): The current floor where the elevator is located.
        destination_floor (int): The floor to which the elevator is heading.
        direction (str): The current direction of the elevator (UP, DOWN, or STOPPED).
        min_floor (int): The minimum floor served by the elevator.
        max_floor (int): The maximum floor served by the elevator.
        max_occupancy (int): The maximum occupancy of the elevator.
        current_occupancy (int): The current number of occupants in the elevator.
    """
    id = models.AutoField(db_column='id', primary_key=True) # primary key
    location = models.CharField(db_column='location', max_length=50, null=True) # location of the elevator
    status = models.ForeignKey('ElevatorStatus', on_delete=models.CASCADE, db_column='status', null=True)
    current_floor = models.IntegerField(db_column='current_floor', null=False) 
    destination_floor = models.IntegerField(db_column='destination_floor', null=True, blank=True)
    direction = models.CharField(max_length=10, choices=[('UP', 'Up'), ('DOWN', 'Down'), ('STOPPED', 'Stopped')]) # True if going up, False if going down
    min_floor = models.IntegerField(db_column='min_floor', null=False) # min floor served by the elevator
    max_floor = models.IntegerField(db_column='max_floor', null=False) # max floor served by the elevator
    max_occupancy = models.IntegerField(db_column='max_occupancy', null=False) # max occupancy of the elevator
    current_occupancy = models.IntegerField(db_column='current_occupancy', null=False) # current occupancy of the elevator


    def __str__(self):
        """
        Returns a string representation of the elevator (its location).
        """
        return str(self.location)
    class Meta:
        db_table = 'elevator'



class ElevatorStatus(models.Model):
    """
    Represents the status of an elevator.

    Attributes:
        id (AutoField): The primary key of the elevator status.
        status (str): The current status of the elevator (BUSY, AVAILABLE, or UNDER_MAINTENANCE).
    """
    id = models.AutoField(db_column='id', primary_key=True) # primary key
    status = models.CharField(max_length=100, choices=[( 'BUSY', 'busy'), ('AVAILABLE' , 'available'), ('UNDER_MAINTENANCE' , 'under_maintenance')]) 
     
    
    def __str__(self):
        """
        Returns a string representation of the elevator status.
        """
        return str(self.status)
    class Meta:
        db_table = 'elevator_status'