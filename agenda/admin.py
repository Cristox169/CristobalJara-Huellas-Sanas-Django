from django.contrib import admin
from .models import Cita, Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "raza", "nombre_dueno")
    search_fields = ("nombre", "nombre_dueno", "especie", "raza")
    list_filter = ("especie",)


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora", "mascota", "dueno", "motivo_consulta", "estado")
    list_filter = ("fecha", "estado")
    search_fields = ("mascota__nombre", "mascota__nombre_dueno", "motivo_consulta")
    date_hierarchy = "fecha"
    list_editable = ("estado",)
    autocomplete_fields = ("mascota",)

    @admin.display(description="Dueño", ordering="mascota__nombre_dueno")
    def dueno(self, obj):
        return obj.mascota.nombre_dueno
