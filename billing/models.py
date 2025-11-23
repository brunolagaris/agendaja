from django.db import models


class StripeEventLog(models.Model):
    event_id = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=100)
    payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(blank=True, null=True)
    error_message = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.type} ({self.event_id})"