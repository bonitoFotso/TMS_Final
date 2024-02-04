from .models import Technicien
from core.utils import MultipleSerializerViewSet
from .filters import TechnicienFilter

from .serializers import (
    TechnicienListSerializer,
    TechnicienDetailSerializer,
    TechnicienCreateSerializer,
    TechnicienUpdateSerializer
)



class TechnicienViewSet(MultipleSerializerViewSet):
    queryset = Technicien.objects.all()
    filterset_class = TechnicienFilter
    serializer_class = TechnicienListSerializer
    serializers = {
        'list': TechnicienListSerializer,
        'retrieve': TechnicienDetailSerializer,
        'create': TechnicienCreateSerializer,
        'update': TechnicienUpdateSerializer,
    }