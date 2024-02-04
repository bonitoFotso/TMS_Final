from .models import Client, Agence, Appelant
from .serializers import ClientListSerializer, ClientDetailSerializer, ClientCreateSerializer, ClientUpdateSerializer
from .serializers import AgenceListSerializer, AgenceDetailSerializer, AgenceCreateSerializer, AgenceUpdateSerializer
from .serializers import AppelantListSerializer, AppelantDetailSerializer, AppelantCreateSerializer, AppelantUpdateSerializer
from core.utils import MultipleSerializerViewSet

class ClientViewSet(MultipleSerializerViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    serializers = {
        'list': ClientListSerializer,
        'retrieve': ClientDetailSerializer,
        'create': ClientCreateSerializer,
        'update': ClientUpdateSerializer,
    }

class AgenceViewSet(MultipleSerializerViewSet):
    queryset = Agence.objects.all()
    serializer_class = AgenceListSerializer
    serializers = {
        'list': AgenceListSerializer,
        'retrieve': AgenceDetailSerializer,
        'create': AgenceCreateSerializer,
        'update': AgenceUpdateSerializer,
    }

class AppelantViewSet(MultipleSerializerViewSet):
    queryset = Appelant.objects.all()
    serializer_class = AppelantListSerializer
    serializers = {
        'list': AppelantListSerializer,
        'retrieve': AppelantDetailSerializer,
        'create': AppelantCreateSerializer,
        'update': AppelantUpdateSerializer,
    }
