from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TechnicienViewSet

# Création d'un routeur
router = SimpleRouter()
router.register(r'techniciens', TechnicienViewSet, basename='technicien')

# Définition des URLs
urlpatterns = [
    path('', include(router.urls)),
]
