from django.contrib.auth.models import User, Group
from rest_framework import serializers
from jokersapp.models import Cliente

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id_Cliente','nom_Cliente','dir_Cliente','ciu_Cliente','tel_Cliente')