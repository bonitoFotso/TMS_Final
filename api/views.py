from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class CurrentTimeUserView(APIView):
    permission_classes = [IsAuthenticated]  # Autoriser uniquement les utilisateurs authentifiés

    def get(self, request):
        # Obtenir l'heure actuelle
        current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        # Obtenir les informations de l'utilisateur authentifié
        user_info = {
            #'username': request.user.username,
            'email': request.user.email,
            # Ajoutez d'autres informations de l'utilisateur que vous souhaitez inclure
        }

        # Renvoyer l'heure actuelle et les informations de l'utilisateur dans la réponse
        return Response({'current_time': current_time, 'user_info': user_info})
