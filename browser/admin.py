from django.contrib import admin

from .models import *


class BarberAdmin(admin.ModelAdmin):
    list_display = ('id', 'barber_name', 'content', 'grade', 'photo', 'clients_count')
    list_display_links = ('id', 'barber_name')
    search_fields = ('barber_name', 'grade')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone', 'visits_count')
    list_display_links = ('id', 'client_name')
    search_fields = ('id', 'client_name', 'phone', 'visits_count')


class VisitAdmin(admin.ModelAdmin):
    list_display = ('barber_id', 'client_id', 'visit_time')
    list_display_links = ('barber_id', 'client_id', 'visit_time')
    search_fields = ('barber_id', 'client_id', 'visit_time')


admin.site.register(Barber, BarberAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Visit, VisitAdmin)
