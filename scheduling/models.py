from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Client(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.owner}"
    

class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=120)
    durations_minutes = models.PositiveIntegerField()
    price_cents = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.owner}"
    
    
class Appointment(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("confirmed", "Confrmed"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
        ("no_show", "No Show"),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, related_name="appointments")
    
    start_datetime = models.DateTimeField()
    end_datetime = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Origem do agendamento (manual, página pública, etc.)
    source = models.CharField(max_length=30, default="manual")
    
    def __str__(self):
        return f"{self.client} - {self.start_datetime} ({self.status})"
    
    
class ReminderLog(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="reminders")
    channel = models.CharField(max_length=20, default="email")
    scheduled_for = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    success = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reminder for {self.appointment} at {self.scheduled_for}."
    