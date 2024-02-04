from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

# Création d'un routeur
router = SimpleRouter()

# Enregistrement des vues avec le routeur
router.register('donneejour', DonneeJourViewSet)
router.register('categorie', CategorieViewSet)
router.register('activite', ActiviteViewSet)
router.register('tache', TacheViewSet)
router.register('technicientache', TechnicienTacheViewSet)
router.register('rapport', RapportViewSet)


urlpatterns = [
    # Autres URL de votre application
    # ...
    # Inclure les URL du routeur dans les URL globales de votre projet
    path('', include(router.urls)),
]
