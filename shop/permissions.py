from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response

class IsAdminAuthenticated(BasePermission):
    """
    Permission personnalisée pour n'autoriser que les utilisateurs administrateurs authentifiés.
    """

    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur est un administrateur authentifié.
        """
        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser:
            # Si l'utilisateur n'est pas un super utilisateur, renvoyer une réponse interdite
            # avec un message d'erreur approprié.
            response = Response({"detail": "Vous n'avez pas les autorisations nécessaires pour accéder à cette ressource."},
                                status=status.HTTP_403_FORBIDDEN)
            raise PermissionDenied(response.data)
        return True
