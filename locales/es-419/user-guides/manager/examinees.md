---
title: "Agrega e importa candidatos en examina.io"
description: "Crea registros de candidatos de forma individual o impórtalos desde archivos de Excel, CSV o texto en examina.io Manager."
tags: [candidate import, csv import, examinees, excel import, manager]
translation_source: user-guides/manager/examinees.md
translation_source_sha256: 173ab50c30199eb9a9667889688609598592bbab3972eab3326f03082ffd9b90
---

# Agrega e importa candidatos

Un **candidato** es la persona que rinde un examen a través de la aplicación Client. Los candidatos son independientes de los **Usuarios** del personal.

![La pestaña Candidatos](../../assets/images/manager/examinees-tab.webp)

## Agrega un candidato

1. Abre **Manager**.
2. Selecciona **Archivo → Agregar nuevo candidato**.
3. Ingresa el nombre y el género del candidato.
4. Ingresa un código único de candidato o elige la asignación automática de código.
5. Ingresa una contraseña o elige la generación de contraseñas.
6. Agrega detalles opcionales como dirección de correo electrónico, número de teléfono, fecha de nacimiento, título o fotografía.
7. Guarda el registro.

El código identifica al candidato al iniciar sesión y debe ser único. Una foto cuadrada de aproximadamente 256 × 256 píxeles funciona mejor cuando tu flujo de trabajo utiliza imágenes de candidatos o verificación de identidad.

![Un registro de candidato guardado](../../assets/images/manager/examinee-details.webp)

## Prepara un archivo de importación

Manager admite:

- Libros de Excel: `.xls` y `.xlsx`
- texto delimitado: `.csv` y `.txt`

Coloca un candidato en cada fila. Los campos obligatorios son:

- nombre;
- apellido; y
- género.

Los códigos y las contraseñas se pueden generar cuando se omiten. Si incluyes números de teléfono, usa el formato internacional, como `+14165550100`. Si incluyes fechas de nacimiento, usa el formato que muestra el importador, como `8/7/1900`.

Para una importación confiable, usa una fila de encabezado con nombres claros de columnas y guarda una copia del archivo de origen original.

Ejemplo de CSV:

```csv
student_id,first_name,last_name,gender,email
STU-1001,Avery,Okafor,F,avery@example.edu
STU-1002,Noah,Martin,M,noah@example.edu
```

## Importa un archivo

1. Selecciona **Archivo → Importar candidatos desde archivo/Excel**.
2. Elige el archivo.
3. Para un archivo de texto, elige o detecta automáticamente el separador, como coma, tabulación, barra vertical, punto y coma o dos puntos.
4. Revisa la vista previa de los datos.
5. Elige si se debe mostrar la segunda línea de vista previa y si la primera fila es un encabezado que se debe omitir.
6. Vincula cada columna de origen con el campo de candidato correspondiente.
7. De forma opcional, elige un Grupo para los registros importados.
8. Elige si el proceso debe detenerse al primer error.
9. Inicia la importación y revisa cada fila agregada, omitida o con error.

Si la opción **Actualizar candidatos existentes si el código/ID del candidato coincide** está disponible y seleccionada, los códigos coincidentes pueden actualizar los registros existentes. Usa esa opción solo cuando el archivo de origen sea de confianza y se haya verificado la vinculación de códigos.

## Valida el resultado

Después de la importación:

- compara la cantidad agregada con el archivo de origen;
- busca varios códigos de candidatos;
- verifica los nombres, direcciones de correo electrónico y las vinculaciones de género;
- revisa cualquier código o contraseña generados automáticamente;
- confirma la pertenencia opcional al Grupo; y
- exporta o registra el historial de importación de acuerdo con tu procedimiento operativo.

Las filas a las que les falten campos obligatorios se omitirán o provocarán la finalización del proceso según la configuración de errores seleccionada.

## Protege los datos de los candidatos

- Importa solo los datos necesarios para administrar la evaluación.
- No coloques contraseñas en una hoja de cálculo compartida públicamente.
- Usa un canal seguro aprobado para distribuir credenciales.
- Elimina los registros de prueba antiguos y las copias locales de acuerdo con tu política de retención.
- Confirma que tu organización tenga una base legal para cualquier foto, dato biométrico o dato de supervisión de exámenes que recopile.

## Siguiente paso

Crea Grupos o asigna candidatos directamente consultando [Grupos y asignaciones de exámenes](groups-and-assignments.md).
