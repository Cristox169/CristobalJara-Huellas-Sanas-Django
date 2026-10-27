from django import forms
from .models import Cita, Mascota


class FormularioMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "nombre_dueno"]
        widgets = {"especie": forms.Select(choices=[("Perro", "Perro"), ("Gato", "Gato"), ("Ave", "Ave"), ("Conejo", "Conejo"), ("Otro", "Otro")])}


class FormularioCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["mascota", "fecha", "hora", "motivo_consulta"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora": forms.TimeInput(attrs={"type": "time"}),
            "motivo_consulta": forms.Textarea(attrs={"rows": 3}),
        }
