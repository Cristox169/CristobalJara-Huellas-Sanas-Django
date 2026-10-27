# Prompts estructurados para la actividad

Estos prompts documentan cómo se puede usar un agente de IA para acelerar el prototipo. Los datos de ejemplo son ficticios; el modelo y las reglas de negocio se implementan y revisan en Django.

## 1. Interfaz web responsive

```text
Rol: Diseñador/a frontend con experiencia en accesibilidad y sistemas de gestión veterinaria.

Objetivo: Proponer HTML semántico y CSS responsive para una aplicación llamada "Huellas Sanas", usada por recepción para registrar pacientes y consultar las citas del día.

Pantallas requeridas:
1. Agenda diaria con selector de fecha, tarjetas de resumen (citas, pendientes, atendidas y pacientes), y tabla con hora, nombre de mascota, especie/raza, responsable, motivo y estado.
2. Formulario de paciente con nombre, especie, raza y nombre del dueño.
3. Formulario de cita con paciente, fecha, hora y motivo.

Restricciones:
- Interfaz en español, clara para recepción y cómoda en escritorio y móvil.
- Usa etiquetas asociadas a controles, foco visible, contraste legible y tablas con encabezados.
- Incluye estados vacíos, errores de validación y confirmación visual.
- Los datos y validaciones vienen del backend Django; no simules persistencia en JavaScript.
- Entrega archivos separados por pantalla y una hoja CSS, con nombres de clases coherentes.
- No agregues librerías externas ni funciones que no estén pedidas.

Criterio de aceptación: en móvil no hay desbordamiento horizontal de la página; la tabla puede desplazarse dentro de su contenedor y los formularios se pueden operar con teclado.
```

## 2. Generación de datos ficticios

```text
Rol: Desarrollador/a Django con experiencia en datos de prueba reproducibles.

Objetivo: Crear un comando de administración Django que genere 20 mascotas y 20 citas ficticias para probar el sistema Huellas Sanas.

Modelos disponibles:
- Mascota(nombre, especie, raza, nombre_dueno)
- Cita(mascota FK, fecha, hora, motivo_consulta, estado)
- estado admite únicamente pendiente, atendida o cancelada.

Requisitos:
- Usa exclusivamente el ORM de Django; no insertes SQL directo.
- Crea nombres, responsables, motivos y especies plausibles pero completamente inventados.
- Incluye citas para hoy y fechas próximas para que la agenda se pueda revisar.
- Evita horarios duplicados en una fecha, respeta las restricciones del modelo y permite ejecutar el comando más de una vez sin duplicar filas.
- Informa al final cuántos registros quedaron cargados.
- No uses datos personales reales ni dependas de paquetes adicionales.

Entrega: código para agenda/management/commands/cargar_datos_demo.py y pasos para correrlo después de migrate.
```

## 3. Administración de citas en Django

```text
Rol: Desarrollador/a backend Django.

Objetivo: configurar Django Admin para que la dirección pueda administrar (crear, consultar, editar y borrar) mascotas y citas.

Requisitos:
- Registra Mascota y Cita en admin.py.
- En citas muestra fecha, hora, mascota, responsable, motivo y estado.
- Agrega filtros por fecha y estado de cita, navegación por fecha y búsqueda por mascota, dueño y motivo.
- Permite cambiar el estado desde el listado y buscar/seleccionar mascotas de forma práctica.
- En mascotas muestra nombre, especie, raza y responsable; permite filtrar por especie y buscar por nombre y responsable.
- Mantén las etiquetas en español.

Entrega: admin.py completo y una breve comprobación manual de las rutas /admin/ y del listado de citas.
```
