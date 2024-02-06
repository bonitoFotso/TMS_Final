from .models import *
from .serializers import *
from .filters import TacheFilter, RapportFilter, TechnicienTacheFilter
from core.utils import MultipleSerializerViewSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TechnicienTache, Tache

class DonneeJourViewSet(MultipleSerializerViewSet):
    queryset = DonneeJour.objects.all()
    serializer_class = DonneeJourListSerializer
    serializers = {
        'list': DonneeJourListSerializer,
        'retrieve': DonneeJourDetailSerializer,
        'create': DonneeJourCreateSerializer,  # Remplacez DonneeJourCreateSerializer par le sérialiseur de création
        'update': DonneeJourUpdateSerializer,  # Remplacez DonneeJourUpdateSerializer par le sérialiseur de modification
    }


class CategorieViewSet(MultipleSerializerViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieListSerializer
    serializers = {
        'list': CategorieListSerializer,
        'retrieve': CategorieDetailSerializer,
        'create': CategorieCreateSerializer,  
        'update': CategorieUpdateSerializer,  
    }


class ActiviteViewSet(MultipleSerializerViewSet):
    queryset = Activite.objects.all()
    serializer_class = ActiviteListSerializer
    serializers = {
        'list': ActiviteListSerializer,
        'retrieve': ActiviteDetailSerializer,
        'create': ActiviteCreateSerializer,  
        'update': ActiviteUpdateSerializer,  
    }


class TacheViewSet(MultipleSerializerViewSet):
    queryset = Tache.objects.all()
    filterset_class = TacheFilter
    serializer_class = TacheListSerializer
    serializers = {
        'list': TacheListSerializer,
        'retrieve': TacheDetailSerializer,
        'create': TacheCreateSerializer,  
        'update': TacheUpdateSerializer,  
    }


class TechnicienTacheViewSet(MultipleSerializerViewSet):
    queryset = TechnicienTache.objects.all()
    serializer_class = TechnicienTacheListSerializer
    filterset_class = TechnicienTacheFilter
    serializers = {
        'list': TechnicienTacheListSerializer,
        'retrieve': TechnicienTacheDetailSerializer,
        'create': TechnicienTacheCreateSerializer,  
        'update': TechnicienTacheUpdateSerializer,  
    }


class RapportViewSet(MultipleSerializerViewSet):
    queryset = Rapport.objects.all()
    filterset_class = RapportFilter
    serializer_class = RapportListSerializer  # Sérialiseur par défaut pour les opérations de liste et de création

    serializers = {
        'list': RapportListSerializer,  # Sérialiseur pour la liste
        'retrieve': RapportDetailSerializer,  # Sérialiseur pour la récupération d'un objet
        'create': RapportCreateSerializer,  # Sérialiseur pour la création d'un objet
        'update': RapportUpdateSerializer,  # Sérialiseur pour la mise à jour complète d'un objet
        'partial_update': RapportUpdateSerializer,  # Sérialiseur pour la mise à jour partielle d'un objet
    }


class TacheTechnicienListView(generics.ListAPIView):
    serializer_class = TacheListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Récupérer l'ID du technicien à partir des paramètres de requête
        technicien_id = self.kwargs.get('technicien_id')
        if technicien_id is not None:
            # Filtrer les tâches pour obtenir celles assignées à ce technicien
            return Tache.objects.filter(assignations__technicien_id=technicien_id)
        else:
            # Si aucun ID de technicien n'est fourni, renvoyer une liste vide
            return Tache.objects.none()
        
class TacheAppelantListView(generics.ListAPIView):
    serializer_class = TacheListSerializer

    def get_queryset(self):
        # Récupérer l'ID de l'appelant à partir des paramètres de requête
        appelant_id = self.kwargs.get('appelant_id')
        # Filtrer les tâches en fonction de l'appelant
        return Tache.objects.filter(appelant_id=appelant_id)