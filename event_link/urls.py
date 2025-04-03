from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView
from .views import ParticipationListCreateView, ParticipationRetrieveUpdateDestroyView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    path('participations/', ParticipationListCreateView.as_view(), name='participation-list-create'),
    path('participations/<int:pk>/', ParticipationRetrieveUpdateDestroyView.as_view(), name='participation-retrieve-update-destroy'),
]
