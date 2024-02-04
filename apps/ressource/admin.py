from django.contrib import admin
from .models import Technicien, StateDay

@admin.register(Technicien)
class TechnicienAdmin(admin.ModelAdmin):
    list_display = ['name', 'prenom', 'matricule', 'tel', 'email', 'date_add', 'date_upd']
    search_fields = ['name', 'prenom', 'matricule', 'tel', 'email']

@admin.register(StateDay)
class StateDayAdmin(admin.ModelAdmin):
    list_display = ['technicien', 'date']
    search_fields = ['technicien__name', 'date']

