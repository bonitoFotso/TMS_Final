from django.urls import path, include
from .views import CurrentTimeUserView


urlpatterns = [
    # Autres URL de votre application
    # ... 
    # Inclure les URL du routeur dans les URL globales de votre projet
    path('api/', include('apps.task.urls')),
    path('api/', include('apps.client.urls')),
    path('api/', include('apps.ressource.urls')),
    path('api/time/', CurrentTimeUserView.as_view(), name='current_time_user'),

]

