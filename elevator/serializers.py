from elevator.models import Elevator
from rest_framework import serializers

class ElevatorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Elevator model.

    This serializer allows converting Elevator instances to JSON and vice versa.

    Attributes:
        model (Elevator): The Elevator model associated with the serializer.
        fields (str or list): The fields to be included in the serialization.
                              If '__all__' is used, all fields from the Elevator model will be included.
    """
    class Meta:
        model = Elevator
        fields = '__all__'