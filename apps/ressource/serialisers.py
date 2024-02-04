from rest_framework import serializers
from .models import Technicien, StateDay


class TechnicienListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technicien
        fields = ['id', 'name', 'prenom', 'tel', 'email', 'matricule']


class TechnicienDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technicien
        fields = '__all__'


class StateDayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateDay
        fields = '__all__'


class StateDayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateDay
        fields = '__all__'
