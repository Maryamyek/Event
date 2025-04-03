from django.contrib import admin
from .models import Event, Participation



class ParticipationInline(admin.TabularInline):  # یا admin.StackedInline
    model = Participation
    extra = 1
    fields = ('user', 'joined_at')
    readonly_fields = ('joined_at',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'start_time', 'end_time', 'capacity', 'created_at', 'updated_at')
    search_fields = ('name', 'location', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    inlines = [ParticipationInline]


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'joined_at')
    search_fields = ('user__username', 'event__name')
    ordering = ('-joined_at',)
    date_hierarchy = 'joined_at'