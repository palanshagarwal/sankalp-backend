from models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'start_date', 'end_date', 'start_time', 'end_time' ,
         'title' , 'venue' , 'description' , 'volunteers')