from django_filters import rest_framework as filters
from .models import Technicien

class TechnicienFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')  # Filtre pour le champ name (recherche insensible à la casse)
    prenom = filters.CharFilter(field_name='prenom', lookup_expr='icontains')  # Filtre pour le champ prenom (recherche insensible à la casse)
    tel = filters.CharFilter(field_name='tel', lookup_expr='icontains')  # Filtre pour le champ tel (recherche insensible à la casse)
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')  # Filtre pour le champ email (recherche insensible à la casse)
    matricule = filters.CharFilter(field_name='matricule', lookup_expr='icontains')  # Filtre pour le champ matricule (recherche insensible à la casse)
    date_add = filters.DateFilter(field_name='date_add', lookup_expr='exact')  # Filtre pour le champ date_add (correspondance exacte)
    date_upd = filters.DateFilter(field_name='date_upd', lookup_expr='exact')  # Filtre pour le champ date_upd (correspondance exacte)
    vitesse_execution = filters.NumberFilter(field_name='vitesse_execution', lookup_expr='exact')  # Filtre pour le champ vitesse_execution (correspondance exacte)
    efficacite = filters.NumberFilter(field_name='efficacite', lookup_expr='exact')  # Filtre pour le champ efficacite (correspondance exacte)

    class Meta:
        model = Technicien
        fields = ['name', 'prenom', 'tel', 'email', 'matricule', 'date_add', 'date_upd', 'vitesse_execution', 'efficacite']
