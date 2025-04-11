from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Event(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    participants = models.ManyToManyField(User, related_name='participated_events', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        open_events_count = Event.objects.filter(
            creator=self.creator,
            status='open'
        ).count()
        if open_events_count >= 5:
            raise ValidationError("You can only have up to 5 open events.")

    class Meta:
        ordering = ['-created_at']
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


# ------------------------------------------------

class Participation(models.Model):
    user = models.ForeignKey(User, related_name='participations', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_participants', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self):
        participation_limit = 5  # حداکثر تعداد ایونت‌هایی که هر کاربر می‌تواند در آن‌ها عضو شود
        user_event_count = Participation.objects.filter(user=self.user).count()
        if user_event_count >= participation_limit:
            raise ValidationError(f"You can only participate in up to {participation_limit} events.")