from tutorial.quickstart.serializers import UserSerializer

from.models import Event, Participation
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['creator', 'name', 'description', 'capacity','start_time', 'end_time', 'location', 'created_at', 'updated_at']
        read_only_fields = ['creator', 'created_at', 'updated_at']






class ParticipationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    class Meta:
        model = Participation
        fields = ['user', 'event', 'joined_at']
        read_only_fields = ['user', 'event', 'joined_at']
