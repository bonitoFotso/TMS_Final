from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

def create_generic_filter(model_class):
    class GenericFilter(filters.FilterSet):
        class Meta:
            model = model_class
            fields = '__all__'

    return GenericFilter


class MultipleSerializerViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)

    serializer_class = {
        'list': None,
        'retrieve': None,
        'create': None,
        'update': None,
    }

    permission_classes = {
        'list': [],
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_class = self.get_filter_class()  # Appel de la méthode get_filter_class() pour obtenir la classe de filtre
        if filter_class:
            return filter_class(self.request.GET, queryset=queryset).qs
        return queryset

    def get_filter_class(self):
        # Si une classe de filtre spécifique est définie pour cette vue, la retourner
        if hasattr(self, 'filterset_class'):
            return self.filterset_class
        # Sinon, retourner la classe de filtre générique
        return create_generic_filter(self.queryset.model)

    def get_serializer_class(self):
        return self.serializers.get(self.action, super().get_serializer_class())

    def get_permissions(self):
        return [permission() for permission in self.permission_classes.get(self.action, [])]