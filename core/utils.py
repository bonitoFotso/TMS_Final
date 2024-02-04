from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions



class MultipleSerializerViewSet(viewsets.ModelViewSet):
    """
    ViewSet utilisant le mixin MultipleSerializerMixin pour gérer plusieurs types de sérialisateurs.
    """
    filter_backends = (filters.DjangoFilterBackend,)

    serializers = {
        'list': None,
        'retrieve': None,
        'create': None,  # Sérialiseur pour la création
        'update': None,  # Sérialiseur pour la modification
    }

    permission_classes = {
        'list': [],  
        'retrieve': [IsAuthenticated],  
        'create': [IsAuthenticated],  # Exemple de permission pour la création
        'update': [IsAuthenticated, DjangoModelPermissions],  # Exemple de permission pour la modification
    }

    def get_serializer_class(self):
        """
        Renvoie la classe de sérialiseur appropriée en fonction de l'action de la vue.
        """
        return self.serializers.get(self.action, super().get_serializer_class())

    def get_permissions(self):
        """
        Renvoie les permissions appropriées en fonction de l'action de la vue.
        """
        return [permission() for permission in self.permission_classes.get(self.action, [])]
