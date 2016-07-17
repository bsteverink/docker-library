from django.db import models

# Create your models here.


class UserProfile(models.Model):
    """User profile"""
    website = models.CharField(max_length=200, verbose_name="website")
