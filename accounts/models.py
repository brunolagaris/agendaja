from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return self.email or self.username
    
    
class Plan(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    price_month_cents = models.PositiveIntegerField(default=0) #em centavos
    max_future_appoiments = models.PositiveIntegerField(null=True, blank=True) # None = ilimitado
    stripe_price_id = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Subscription(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("past_due", "Past due"),
        ("canceled", "Canceled"),
    ]
    
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="inactive")
    current_period_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.plan} ({self.status})"