from rest_framework import serializers
from .models import Client, Agence, Appelant
from rest_framework import serializers
from .models import Client

class AppelantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'

class AgenceSerializer(serializers.ModelSerializer):
    appelants = AppelantSerializer(many=True, read_only=True)
    class Meta:
        model = Agence
        fields = '__all__'



class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    agences = AgenceSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

from rest_framework import serializers
from .models import Agence

class AgenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'

class AgenceDetailSerializer(serializers.ModelSerializer):
    appelants = AppelantSerializer(many=True, read_only=True)

    class Meta:
        model = Agence
        fields = '__all__'

class AgenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'

class AgenceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = '__all__'

from rest_framework import serializers
from .models import Appelant

class AppelantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'

class AppelantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'

class AppelantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'

class AppelantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appelant
        fields = '__all__'
