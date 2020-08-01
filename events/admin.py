from django.contrib import admin
from .models import Event, Attendee

# Register your models here.
class EventAdmin(admin.ModelAdmin):
  list_display = ['id', 'slug', 'event_date', 'featured']
  list_display_links = ['id', 'slug']
  list_editable = ['featured']
  list_filter = ['slug', 'event_date']
  list_per_page = 25


admin.site.register(Event, EventAdmin)
admin.site.register(Attendee)