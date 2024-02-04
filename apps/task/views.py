from .models import *
from .serializers import *
from .filters import TacheFilter, RapportFilter, TechnicienTacheFilter
from core.utils import MultipleSerializerViewSet


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


