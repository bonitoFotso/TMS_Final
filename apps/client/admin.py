from django.contrib import admin
from .models import Client, Agence, Appelant

class AppelantInline(admin.TabularInline):
    model = Appelant
    extra = 1

class AgenceInline(admin.TabularInline):
    model = Agence
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [AgenceInline]
    list_display = ['name', 'responsable', 'email', 'phone', 'address', 'city', 'n_client', 'maintenance']
    search_fields = ['name', 'responsable', 'email', 'phone', 'address', 'city', 'n_client']
    list_filter = ['maintenance']
    readonly_fields = ['n_client']
    ordering = ['name']

@admin.register(Agence)
class AgenceAdmin(admin.ModelAdmin):
    inlines = [AppelantInline]
    list_display = ['name', 'responsable', 'email', 'phone', 'address', 'city', 'n_agence', 'siege']
    search_fields = ['name', 'responsable', 'email', 'phone', 'address', 'city', 'n_agence']
    list_filter = ['siege']
    readonly_fields = ['n_agence']
    ordering = ['name']

@admin.register(Appelant)
class AppelantAdmin(admin.ModelAdmin):
    list_display = ['name', 'agence', 'phone', 'email', 'addAt', 'updAt']
    search_fields = ['name', 'agence__name', 'phone', 'email']
    list_filter = ['agence']
    ordering = ['name']
