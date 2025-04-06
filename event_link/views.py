from .models import Event, Participation
from .serializers import EventSerializer, ParticipationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework import generics, status
from rest_framework.response import Response




# View برای مدیریت ایونت‌ها
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(creator=self.request.user)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        # جلوگیری از حذف ایونت‌های دارای شرکت‌کننده‌ها
        if instance.participants.exists():
            return Response({"error": "You cannot delete an event with participants."},
                            status=status.HTTP_400_BAD_REQUEST)
        instance.delete()

# ---------------------------------

# View برای مدیریت شرکت‌کنندگان
class ParticipationListCreateView(generics.ListCreateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    # permissions_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------

class ParticipationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    # permission_classes = [permissions.IsAuthenticated]