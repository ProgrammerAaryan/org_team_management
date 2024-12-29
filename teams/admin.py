# teams/admin.py
from django.contrib import admin
from .models import Organization, Team, Member

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'location', 'description']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'description']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'unique_id', 'team', 'profile_image']
    list_filter = ['team']
