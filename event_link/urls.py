from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView
from .views import ParticipationListCreateView, ParticipationRetrieveUpdateDestroyView, JoinEventView, LeaveEventView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    path('participations/', ParticipationListCreateView.as_view(), name='participation-create'),  # برای ایجاد مشارکت
    path('participations/<int:pk>/', ParticipationRetrieveUpdateDestroyView.as_view(), name='participation-retrieve-update-destroy'),
    path('join-event/', JoinEventView.as_view(), name='join-event'),
    path('leave-event/<int:event_id>/', LeaveEventView.as_view(), name='leave-event'),
]
