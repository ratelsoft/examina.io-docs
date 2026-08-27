---
title: "Importa un examen en Manager de examina.io"
description: "Exporta una evaluación .smex desde Designer, impórtala en Manager y verifica el examen antes de asignar candidatos."
tags: [designer export, exam import, manager, smex]
translation_source: user-guides/manager/import-exams.md
translation_source_sha256: cdd0384f56afe40f416a9be4f57bf31c41f1b3b32098cafb860f785f7f9aa421
---

# Importa un examen en Manager

Manager acepta paquetes de exámenes exportados por Designer como archivos `.smex`. Importa el paquete antes de agregar asignaciones o compartir un enlace al examen.

## Antes de importar

En Designer, confirma:

- que el título y el código del examen sean correctos;
- que cada prueba contenga las preguntas previstas;
- que la duración de la prueba y la configuración de preguntas a responder sean correctas;
- que la puntuación y las respuestas correctas se hayan revisado;
- que las instrucciones y las reglas de navegación estén completas; y
- que el proyecto se haya guardado antes de exportar.

Conserva el proyecto de origen como tu versión maestra editable. El archivo `.smex` exportado es el paquete de aplicación.

## Importa el archivo

![Archivo → Agregar nuevo examen](../../assets/images/manager/file-menu.png)

1. Abre **Manager**.
2. Selecciona **Archivo → Agregar nuevo examen**.
3. Arrastra el archivo `.smex` al área de carga o selecciónalo con el selector de archivos.
4. Envía la carga.
5. Espera el mensaje de confirmación que contiene el código y el título del examen importado.

Si Manager indica que el tipo de archivo no es compatible, regresa a Designer y exporta el examen en el formato `.smex` compatible. Si el archivo supera el tamaño permitido para tu entorno o plan, reduce los archivos multimedia de gran tamaño y vuelve a exportarlo.

## Verifica el examen importado

Selecciona el examen y revisa su panel de detalles:

![Detalles del examen importado](../../assets/images/manager/exam-details.png)

- título, código y versión del examen;
- flujo de la prueba del examen;
- visibilidad;
- tamaño del archivo importado; y
- la hora en que se agregó.

**Tamaño del archivo del examen** es la comprobación más rápida para verificar que llegó el paquete correcto; una cifra mucho menor de lo esperado generalmente significa que a la exportación le faltan archivos multimedia.

Abre la información de la prueba y compárala con el proyecto de Designer. No asignes candidatos reales hasta que el contenido y los tiempos sean correctos.

## Actualiza un examen de forma segura

Si el contenido cambia después de la importación:

1. Actualiza y valida el proyecto de origen en Designer.
2. Exporta un nuevo archivo de aplicación.
3. Impórtalo según el proceso de cambios de tu organización.
4. Vuelve a comprobar las asignaciones, la visibilidad, la supervisión de exámenes y la comunicación antes de la publicación.

No asumas que un archivo recién exportado conservará cada configuración del lado de la entrega. Verifica el registro en Manager y prueba el recorrido en Client después de cualquier reemplazo o cambio de versión.

## Continúa con la configuración

A continuación, [agrega o importa candidatos](examinees.md) y luego [asigna personas y pruebas](groups-and-assignments.md).
