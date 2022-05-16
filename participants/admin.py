from django.contrib import admin
from participants.models import Participant, ParticipantRole

class RolesAdmin(admin.ModelAdmin):
    list_display = ['role']

class PartAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'role']

admin.site.register(Participant, PartAdmin)
admin.site.register(ParticipantRole, RolesAdmin)