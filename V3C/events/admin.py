from django.contrib import admin
from events.models import Conference
# Register your models here.
class ConfAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time', 'con_reference', 'con_pass', 'notes']

admin.site.register(Conference, ConfAdmin)
