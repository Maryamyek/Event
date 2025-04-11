from.models import Event, Participation
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['creator', 'name', 'description', 'capacity','start_time', 'end_time', 'location', 'created_at', 'updated_at']
        read_only_fields = ['creator', 'created_at', 'updated_at']








class ParticipationSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), required=True)
    class Meta:
        model = Participation
        fields = ['event']


        def validate_event(self, value):
            # اعتبارسنجی کمپنی در ایونت
            if not Event.objects.filter(id=value.id, status='open').exists():
                raise serializers.ValidationError("This event is not available for joining.")

            return value

# -------------------------

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'capacity', 'start_time', 'end_time', 'location']

