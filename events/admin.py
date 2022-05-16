from django.contrib import admin
from events.models import Conference
from events.forms import *
# Register your models here.
class ConfAdmin(admin.ModelAdmin):
    form = EventChangeForm
    add_form = EventCreationForm
    list_display = ['name', 'start_time', 'end_time', 'con_reference', 'con_pass', 'notes', 'is_active']

    search_fields = ('name', 'start_time', 'end_time')
    ordering = ('name', 'start_time', 'end_time', 'is_active')

admin.site.register(Conference, ConfAdmin)
