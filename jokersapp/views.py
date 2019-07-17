from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from jokersapp.serializers import UserSerializer, GroupSerializer
from jokersapp.models import *
from jokersapp.serializers import ClienteSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView,UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def home(request):
    return HttpResponse('Vista Home!')

class ArticuloListView(LoginRequiredMixin,ListView):
    model = Articulo

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente

class FacturaListView(LoginRequiredMixin,ListView):
    model = Factura

class DetalleListView(LoginRequiredMixin,ListView):
    model = Detalle

class ProveedorListView(LoginRequiredMixin,ListView):
    model = Proveedor

class CompraListView(LoginRequiredMixin,ListView):
    model = Compra

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

class ArticuloCreate(LoginRequiredMixin,CreateView):
    model = Articulo
    fields = '__all__'

class ClienteCreate(LoginRequiredMixin,CreateView):
    model = Cliente
    fields = '__all__'

class FacturaCreate(LoginRequiredMixin,CreateView):
    model = Factura
    fields = '__all__'

class DetalleCreate(LoginRequiredMixin,CreateView):
    model = Detalle
    fields = '__all__'

class ProveedorCreate(LoginRequiredMixin,CreateView):
    model = Proveedor
    fields = '__all__'

class CompraCreate(LoginRequiredMixin,CreateView):
    model = Compra
    fields = '__all__'

