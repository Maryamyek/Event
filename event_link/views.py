from .models import Event, Participation
from .serializers import EventSerializer, ParticipationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError as DRFValidationError



# View برای مدیریت ایونت‌ها
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(status='open')
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        try:
            serializer.save(creator=self.request.user)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

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
            serializer.save(user=self.request.user)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------

class ParticipationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    # permission_classes = [permissions.IsAuthenticated]

# -----------------------------------

class JoinEventView(generics.CreateAPIView):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        # بررسی ظرفیت ایونت
        if event.participants.count() >= event.capacity:
            raise DRFValidationError("Event capacity is full.")
        # بررسی محدودیت تعداد ایونت‌ها
        participation_limit = 5
        user_event_count = Participation.objects.filter(user=self.request.user).count()
        if user_event_count >= participation_limit:
            raise DRFValidationError(f"You can only participate in up to {participation_limit} events.")
        # اگر همه شرایط درست باشد، شرکت کننده را اضافه کنید
        serializer.save(user=self.request.user)

# -------------------------------------

class LeaveEventView(generics.DestroyAPIView):
    queryset = Participation.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # استفاده از filter به جای get
        participation = Participation.objects.filter(user=self.request.user, event_id=self.kwargs['event_id']).first()
        if not participation:
            raise NotFound("You are not a participant in this event.")
        return participation