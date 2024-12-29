# teams/models.py
from django.db import models
import uuid
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField(default='example@example.com')
    location = models.CharField(max_length=255, default="Unknown Location")

    def __str__(self):
        return self.name

class Team(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Image upload field

    def __str__(self):
        return self.name
