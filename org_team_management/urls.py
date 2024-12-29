# your_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from teams.views import org_team_member_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', include('teams.urls')),  # Include the teams app URLs
     path('', include('teams.urls')),
      path('', org_team_member_list, name='home'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)