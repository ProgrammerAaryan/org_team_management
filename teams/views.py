# teams/views.py
from django.shortcuts import render, redirect
from .models import Organization
from .forms import MemberForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer


def org_team_member_list(request):
    organizations = Organization.objects.all()
    return render(request, 'teams/org_team_member_list.html', {'organizations': organizations})

def member_upload(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('org_team_member_list')
    else:
        form = MemberForm()
    return render(request, 'teams/member_upload.html', {'form': form})

class MemberListView(APIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)