from django.contrib import admin
from .models import Track

# Register your models here.
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = 20
