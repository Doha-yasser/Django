from django.contrib import admin
from .models import Trainee

# Register your models here.
@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'track', 'phone', 'created_at']
    list_filter = ['track', 'created_at']
    search_fields = ['name', 'email']
    list_per_page = 20
