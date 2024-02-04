from django_filters import rest_framework as filters
from .models import Tache, Rapport, TechnicienTache


class TacheFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Filtre pour le champ name (recherche insensible à la casse)
    status = filters.CharFilter(lookup_expr='exact')  # Filtre pour le champ status (correspondance exacte)
    appelant = filters.CharFilter(field_name='appelant__name', lookup_expr='icontains')  # Filtre pour le champ appelant (recherche insensible à la casse, utilise le champ name de la relation)
    priorite = filters.CharFilter(lookup_expr='exact')  # Filtre pour le champ priorite (correspondance exacte)
    description = filters.CharFilter(lookup_expr='icontains')  # Filtre pour le champ description (recherche insensible à la casse)
    n_OS = filters.CharFilter(lookup_expr='exact')  # Filtre pour le champ n_OS (correspondance exacte)
    ok = filters.BooleanFilter(field_name='ok', lookup_expr='exact')  # Filtre pour le champ ok (correspondance exacte)
    date_debut = filters.DateFilter(field_name='date_debut', lookup_expr='exact')  # Filtre pour le champ date_debut (correspondance exacte)
    date_fin = filters.DateFilter(field_name='date_fin', lookup_expr='exact')  # Filtre pour le champ date_fin (correspondance exacte)
    duree_estimee = filters.DurationFilter(field_name='duree_estimee', lookup_expr='exact')  # Filtre pour le champ duree_estimee (correspondance exacte)
    duree_reelle = filters.DurationFilter(field_name='duree_reelle', lookup_expr='exact')  # Filtre pour le champ duree_reelle (correspondance exacte)
    createdAt = filters.DateFilter(field_name='createdAt', lookup_expr='exact')  # Filtre pour le champ createdAt (correspondance exacte)
    updatedAt = filters.DateFilter(field_name='updatedAt', lookup_expr='exact')  # Filtre pour le champ updatedAt (correspondance exacte)
    assignations = filters.CharFilter(field_name='assignations__name', lookup_expr='icontains')  # Filtre pour le champ assignations (recherche insensible à la casse, utilise le champ name de la relation)

    class Meta:
        model = Tache
        fields = ['name', 'status', 'appelant', 'priorite', 'description', 'n_OS', 'ok', 'date_debut', 'date_fin', 'duree_estimee', 'duree_reelle', 'createdAt', 'updatedAt', 'assignations']

class RapportFilter(filters.FilterSet):
    rapport_text = filters.CharFilter(field_name='rapport_text', lookup_expr='icontains')  # Filtre pour le champ rapport_text (recherche insensible à la casse)
    technicien_list = filters.CharFilter(field_name='technicien_list', lookup_expr='icontains')  # Filtre pour le champ technicien_list (recherche insensible à la casse)
    date_creation = filters.DateFilter(field_name='date_creation', lookup_expr='exact')  # Filtre pour le champ date_creation (correspondance exacte)

    class Meta:
        model = Rapport
        fields = ['rapport_text', 'technicien_list', 'date_creation']

class TechnicienTacheFilter(filters.FilterSet):
    ok = filters.BooleanFilter(field_name='ok', lookup_expr='exact')  # Filtre pour le champ ok (correspondance exacte)
    date_debut = filters.DateFilter(field_name='date_debut', lookup_expr='exact')  # Filtre pour le champ date_debut (correspondance exacte)
    date_fin = filters.DateFilter(field_name='date_fin', lookup_expr='exact')  # Filtre pour le champ date_fin (correspondance exacte)
    createdAt = filters.DateFilter(field_name='createdAt', lookup_expr='exact')  # Filtre pour le champ createdAt (correspondance exacte)

    class Meta:
        model = TechnicienTache
        fields = ['ok', 'date_debut', 'date_fin', 'createdAt']