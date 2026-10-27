from datetime import date, time, timedelta
from django.core.management.base import BaseCommand
from agenda.models import Cita, Mascota


class Command(BaseCommand):
    help = "Crea de forma repetible 20 mascotas ficticias y sus citas iniciales."

    def handle(self, *args, **options):
        pacientes = [
            ("Luna", "Perro", "Mestiza", "Camila Rojas"),
            ("Milo", "Gato", "Naranjo", "Diego Fuentes"),
            ("Nala", "Perro", "Labrador", "Valentina Soto"),
            ("Toby", "Perro", "Poodle", "Andrés Silva"),
            ("Mora", "Gato", "Carey", "Fernanda Díaz"),
            ("Coco", "Conejo", "Enano", "Martín Pérez"),
            ("Rocky", "Perro", "Bulldog", "Daniela Muñoz"),
            ("Simba", "Gato", "Siamés", "Javiera Torres"),
            ("Kira", "Perro", "Pastor alemán", "Nicolás Vega"),
            ("Pepita", "Ave", "Canario", "Paula Castillo"),
            ("Bruno", "Perro", "Golden retriever", "Ignacio Reyes"),
            ("Michi", "Gato", "Doméstico", "Antonia Morales"),
            ("Chispa", "Conejo", "Cabeza de león", "Tomás Herrera"),
            ("Rocco", "Perro", "Beagle", "Francisca Navarro"),
            ("Olivia", "Gato", "Persa", "Sebastián Vidal"),
            ("Pipo", "Ave", "Periquito", "Isidora Campos"),
            ("Doki", "Perro", "Shih tzu", "Benjamín Castro"),
            ("Maya", "Gato", "Tricolor", "Catalina Flores"),
            ("Chester", "Perro", "Cocker spaniel", "Matías Contreras"),
            ("Pelusa", "Conejo", "Angora", "Josefa Álvarez"),
        ]
        motivos = [
            "Control preventivo anual", "Vacunación", "Consulta dermatológica", "Control de peso",
            "Molestia digestiva", "Revisión dental", "Chequeo general", "Seguimiento de tratamiento",
            "Limpieza de oídos", "Evaluación de movilidad", "Vacunación y desparasitación",
            "Irritación ocular", "Corte de uñas", "Tos y estornudos", "Control postoperatorio",
            "Consulta preventiva", "Picazón persistente", "Examen de rutina", "Dolor en una pata", "Revisión general",
        ]
        estados = [Cita.Estado.PENDIENTE, Cita.Estado.ATENDIDA, Cita.Estado.PENDIENTE,
                   Cita.Estado.PENDIENTE, Cita.Estado.CANCELADA]
        mascotas = []
        for nombre, especie, raza, dueno in pacientes:
            mascota, _ = Mascota.objects.update_or_create(
                nombre=nombre, nombre_dueno=dueno,
                defaults={"especie": especie, "raza": raza},
            )
            mascotas.append(mascota)

        hoy = date.today()
        horas = [time(9, 0), time(9, 30), time(10, 0), time(10, 30), time(11, 0),
                 time(11, 30), time(12, 0), time(12, 30), time(14, 0), time(14, 30),
                 time(15, 0), time(15, 30), time(16, 0), time(16, 30), time(17, 0)]
        for i, mascota in enumerate(mascotas):
            offset = 0 if i < 8 else (1 if i < 15 else 2)
            fecha = hoy + timedelta(days=offset)
            Cita.objects.update_or_create(
                fecha=fecha, hora=horas[i % len(horas)],
                defaults={
                    "mascota": mascota,
                    "motivo_consulta": motivos[i],
                    "estado": estados[i % len(estados)],
                },
            )
        self.stdout.write(self.style.SUCCESS(
            f"Datos listos: {Mascota.objects.count()} mascotas y {Cita.objects.count()} citas en total."
        ))
