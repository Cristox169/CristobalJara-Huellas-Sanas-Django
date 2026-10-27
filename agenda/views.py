from datetime import date
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_date
from .forms import FormularioCita, FormularioMascota
from .models import Cita, Mascota


def agenda_diaria(request):
    seleccion = parse_date(request.GET.get("fecha", "")) or date.today()
    citas = Cita.objects.filter(fecha=seleccion).select_related("mascota")
    return render(request, "agenda/inicio.html", {
        "citas": citas, "fecha": seleccion,
        "total": citas.count(),
        "pendientes": citas.filter(estado=Cita.Estado.PENDIENTE).count(),
        "atendidas": citas.filter(estado=Cita.Estado.ATENDIDA).count(),
        "mascotas_total": Mascota.objects.count(),
    })


def nueva_mascota(request):
    form = FormularioMascota(request.POST or None)
    if request.method == "POST" and form.is_valid():
        mascota = form.save()
        messages.success(request, f"{mascota.nombre} quedó registrado/a.")
        return redirect("nueva_cita_mascota", mascota_id=mascota.pk)
    return render(request, "agenda/formulario_mascota.html", {"form": form})


def nueva_cita(request, mascota_id=None):
    mascota_inicial = get_object_or_404(Mascota, pk=mascota_id) if mascota_id else None
    form = FormularioCita(request.POST or None, initial={"mascota": mascota_inicial})
    if mascota_inicial:
        form.fields["mascota"].initial = mascota_inicial
    if request.method == "POST" and form.is_valid():
        try:
            cita = form.save()
        except IntegrityError:
            form.add_error("hora", "Ya existe una cita para ese día y hora. Elige otro bloque.")
        else:
            messages.success(request, f"Cita agendada para {cita.mascota.nombre} el {cita.fecha:%d-%m-%Y}.")
            return redirect("agenda")
    return render(request, "agenda/formulario_cita.html", {"form": form, "mascota": mascota_inicial})
