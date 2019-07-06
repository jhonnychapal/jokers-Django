from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from jokersapp.serializers import UserSerializer, GroupSerializer
from jokersapp.models import Cliente
from jokersapp.serializers import ClienteSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def base(request):
    return render(request, 'base.html')

def home(request):
    return HttpResponse('Vista Home!')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allosw groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

