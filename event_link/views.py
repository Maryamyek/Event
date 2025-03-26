from .models import Event, Participation
from .serializers import EventSerializer, ParticipationSerializer
from django.shortcuts import render
from rest_framework import generics, permissions


# برای مدیریت شرکت کنندگان
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

# برای مدیریت شرکت کنندگان
class ParticipationList(generics.ListCreateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParticipationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]
