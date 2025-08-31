from django.db import models
from track.models import Track

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='trainees')
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
