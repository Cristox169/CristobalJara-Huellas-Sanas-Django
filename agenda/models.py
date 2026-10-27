from django.core.validators import MinLengthValidator
from django.db import models


class Mascota(models.Model):
    nombre = models.CharField("nombre", max_length=80)
    especie = models.CharField("especie", max_length=40)
    raza = models.CharField("raza", max_length=60, blank=True)
    nombre_dueno = models.CharField("nombre del dueño", max_length=120)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"

    def __str__(self):
        return f"{self.nombre} · {self.especie}"


class Cita(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        ATENDIDA = "atendida", "Atendida"
        CANCELADA = "cancelada", "Cancelada"

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="citas", verbose_name="mascota")
    fecha = models.DateField("fecha")
    hora = models.TimeField("hora")
    motivo_consulta = models.CharField("motivo de consulta", max_length=240, validators=[MinLengthValidator(3)])
    estado = models.CharField("estado", max_length=12, choices=Estado.choices, default=Estado.PENDIENTE)

    class Meta:
        ordering = ["fecha", "hora"]
        verbose_name = "cita"
        verbose_name_plural = "citas"
        constraints = [models.UniqueConstraint(fields=["fecha", "hora"], name="una_cita_por_bloque_horario")]

    def __str__(self):
        return f"{self.fecha:%d-%m-%Y} {self.hora:%H:%M} · {self.mascota.nombre}"
