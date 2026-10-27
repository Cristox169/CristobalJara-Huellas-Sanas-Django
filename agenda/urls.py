from django.urls import path
from . import views

urlpatterns = [
    path("", views.agenda_diaria, name="agenda"),
    path("mascotas/nueva/", views.nueva_mascota, name="nueva_mascota"),
    path("citas/nueva/", views.nueva_cita, name="nueva_cita"),
    path("mascotas/<int:mascota_id>/cita/", views.nueva_cita, name="nueva_cita_mascota"),
]
