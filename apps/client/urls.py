from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet, AgenceViewSet, AppelantViewSet

# Création d'un routeur
router = SimpleRouter()

# Enregistrement des vues avec le routeur
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'agences', AgenceViewSet, basename='agence')
router.register(r'appelants', AppelantViewSet, basename='appelant')

# URL globales de l'application
urlpatterns = [
    path('', include(router.urls)),
]
