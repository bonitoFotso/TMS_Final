from django.urls import path, include
from .views import CurrentTimeUserView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # Autres URL de votre application
    # ... 
    # Inclure les URL du routeur dans les URL globales de votre projet
    path('api/', include('apps.task.urls')),
    path('api/', include('apps.client.urls')),
    path('api/', include('apps.ressource.urls')),
    path('api/time/', CurrentTimeUserView.as_view(), name='current_time_user'),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]

