from rest_framework import generics, permissions
from .models import Event, Participation
from .serializers import EventSerializer, ParticipationSerializer

# View برای مدیریت ایونت‌ها
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

# View برای مدیریت شرکت‌کنندگان
class ParticipationListCreateView(generics.ListCreateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    # permissions_classes = [permissions.IsAuthenticated]

class ParticipationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    # permission_classes = [permissions.IsAuthenticated]