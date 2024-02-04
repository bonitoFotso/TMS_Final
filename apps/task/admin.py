from django.contrib import admin
from .models import Tache, TechnicienTache, Rapport

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'date_debut', 'date_fin']
    list_filter = ['status']
    search_fields = ['name']

@admin.register(TechnicienTache)
class TechnicienTacheAdmin(admin.ModelAdmin):
    list_display = ['technicien', 'tache', 'ok', 'date_debut', 'date_fin']
    list_filter = ['ok']
    search_fields = ['technicien__name', 'tache__name']

@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    list_display = ['tache', 'date_creation']
    search_fields = ['tache__name']

from django.contrib import admin
from .models import Categorie, Activite

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'createdAt', 'updatedAt')
    search_fields = ('name', 'description')
    list_filter = ('createdAt', 'updatedAt')
    readonly_fields = ('createdAt', 'updatedAt')

@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'createdAt', 'updatedAt')
    search_fields = ('name', 'description')
    list_filter = ('createdAt', 'updatedAt')
    readonly_fields = ('createdAt', 'updatedAt')
