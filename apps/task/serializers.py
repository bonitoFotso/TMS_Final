from rest_framework import serializers
from .models import *
from apps.ressource.serializers import TechnicienListSerializer
from apps.client.serializers import AppelantDetailSerializer


class DonneeJourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeJour
        fields = '__all__'


class CategorieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ActiviteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'


class TacheListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class TechnicienTacheListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicienTache
        fields = '__all__'


class RapportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'


class DonneeJourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeJour
        fields = '__all__'


class CategorieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ActiviteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'


class TacheDetailSerializer(serializers.ModelSerializer):
    activite = ActiviteListSerializer(many=True)
    categorie = CategorieListSerializer(many=True)
    assignations = TechnicienTacheListSerializer(many=True)
    appelant = AppelantDetailSerializer()

    class Meta:
        model = Tache
        fields = '__all__'


class TechnicienTacheDetailSerializer(serializers.ModelSerializer):
    technicien = TechnicienListSerializer()
    tache = TacheListSerializer()

    class Meta:
        model = TechnicienTache
        fields = '__all__'


class RapportDetailSerializer(serializers.ModelSerializer):
    tache = TacheListSerializer()

    class Meta:
        model = Rapport
        fields = '__all__'


from rest_framework import serializers
from .models import *


class DonneeJourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeJour
        fields = '__all__'


class DonneeJourUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeJour
        fields = '__all__'


class CategorieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class CategorieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ActiviteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'


class ActiviteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = '__all__'


class TacheCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class TacheUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class TechnicienTacheCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicienTache
        fields = '__all__'


class TechnicienTacheUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicienTache
        fields = '__all__'


class RapportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'


class RapportUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'
