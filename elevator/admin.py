from django.contrib import admin

# Register your models here.
from elevator.models import Elevator, ElevatorStatus


admin.site.register(Elevator) # register the Elevator model in the admin site
admin.site.register(ElevatorStatus)