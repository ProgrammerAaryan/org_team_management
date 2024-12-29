# teams/urls.py
from django.urls import path
from . import views
from .views import MemberListView

urlpatterns = [
    path('', views.org_team_member_list, name='org_team_member_list'),
    path('upload/', views.member_upload, name='member_upload'),
     path('api/members/', MemberListView.as_view(), name='member-list'),
]
