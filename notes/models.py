from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userNote", null=True)

    
    class Meta:
        ordering = ('title',)
