from django.urls import path, include


urlpatterns = [
    # Autres URL de votre application
    # ...
    # Inclure les URL du routeur dans les URL globales de votre projet
    path('api/', include('apps.task.urls')),
]