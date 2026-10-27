# Huellas Sanas - agenda veterinaria

Aplicación Django para gestionar mascotas, citas veterinarias y la agenda diaria. Incluye formularios para recepción, Django Admin, control de choques de horario y un comando para cargar datos de demostración.

## Requisitos

- Python 3.10 o posterior
- Windows PowerShell o una terminal compatible

## Instalación y ejecución en Windows

Abre una terminal en la carpeta que contiene `manage.py` y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos_demo
python manage.py runserver
```

Cuando el servidor esté listo, la terminal mostrará los enlaces directos a la página y al panel de administración:

- Página Huellas Sanas: <http://127.0.0.1:8000/>
- Panel de administración: <http://127.0.0.1:8000/admin/>

Abre el primer enlace en el navegador. Mantén la terminal abierta mientras uses la página. Para entrar al panel Admin, crea tu usuario con `python manage.py createsuperuser`.

Si aparece un error que indica que el puerto 8000 está ocupado, ejecuta `python manage.py runserver 8001`; los enlaces impresos usarán el nuevo puerto.

## Qué incluye

- Registro de mascotas y citas.
- Agenda diaria con resumen por estado.
- Validación para evitar dos citas en la misma fecha y hora.
- Administración de mascotas y citas con filtros por fecha y estado.
- Datos ficticios de 20 pacientes disponibles mediante `python manage.py cargar_datos_demo`.
- Prompts estructurados de apoyo en [`docs/prompts_ia.md`](docs/prompts_ia.md).

El ZIP incluye una base SQLite de demostración, preparada con 20 mascotas y 20 citas ficticias para que la página cargue al iniciar. No contiene usuarios ni contraseñas de acceso al Admin. Al clonar desde GitHub, el archivo de base de datos no estará incluido; ejecuta las instrucciones de instalación de arriba para crearla.
