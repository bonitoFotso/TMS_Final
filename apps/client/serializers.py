from rest_framework import serializers
from .models import Client, Agence, Appelant

class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'responsable', 'email', 'phone', 'address', 'city', 'n_client', 'maintenance']

class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AgenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = ['id', 'name', 'responsable', 'email', 'phone', 'address', 'city', 'n_agence', 'siege']

class AgenceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'

class AppelantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = ['id', 'name', 'agence', 'phone', 'email', 'addAt', 'updAt']

class AppelantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'
