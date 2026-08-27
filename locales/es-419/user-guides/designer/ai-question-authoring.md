---
title: "Crea preguntas de examen respaldadas por fuentes con IA"
description: "Redacta preguntas de examen editables y con citas desde PDF, DOCX, PPTX, TXT, Markdown, HTML y pasajes con Designer de examina.io."
tags: [source-backed AI question authoring, assessment authoring, exam questions, Designer, cited questions]
translation_source: user-guides/designer/ai-question-authoring.md
translation_source_sha256: f2eee7ab06512f6877e0dc625ad4ff119520e39668d030b899bc4d144b41b991
---

# Crea y revisa preguntas con IA

Designer puede convertir el material de origen en borradores de preguntas editables sin salir de la prueba actual. Nunca inserta ni publica el contenido generado por IA de forma automática: un autor autorizado revisa cada candidato y elige qué se incluye en la prueba.

## Qué incluye tu plan y cuánto cuestan las preguntas adicionales

La creación de preguntas con IA respaldadas por fuentes está incluida en todos los planes. Tu cuota mensual contabiliza los candidatos válidos, respaldados por fuentes y no duplicados que llegan a **Review**; no las solicitudes, las páginas cargadas ni los reintentos del proveedor.

| Plan | Preguntas respaldadas por fuentes al mes | Almacenamiento de la biblioteca de fuentes | Fuentes guardadas | Tamaño máximo de archivo |
| --- | ---: | ---: | ---: | ---: |
| Starter | 10 | 250 MB | 25 | 50 MB |
| Basic | 100 | 2 GB | 250 | 250 MB |
| Professional | 500 | 10 GB | 1,000 | 500 MB |
| Flexible | 100 | 5 GB | 500 | 500 MB |
| Enterprise | Personalizado | Personalizado | Personalizado | Personalizado |

La cuota incluida se reinicia al principio de cada mes calendario UTC y la comparte la organización. La cuota actual se muestra en la ventana de creación con IA. Una pregunta de solo texto o una pregunta que reutiliza una imagen de la fuente consume una pregunta incluida. Una pregunta con un elemento visual recién generado consume cuatro preguntas incluidas. Por ejemplo, una cuota de 100 puede producir hasta 100 preguntas de texto o con imágenes de la fuente, hasta 25 preguntas con elementos visuales recién generados, o una combinación de ambas.

Una vez consumida la cuota incluida, el precio actual de cada pregunta válida adicional que llegue a Review es:

| Resultado que llega a Review | USD | CAD | NGN |
| --- | ---: | ---: | ---: |
| Pregunta de solo texto o con imagen de la fuente | $0.15 | C$0.20 | ₦200 |
| Pregunta con un elemento visual recién generado | $0.60 | C$0.80 | ₦800 |

No existe un producto de créditos de IA ni un monedero de IA independiente. El precio se reserva y se descuenta del saldo prepago normal de tu organización. Todos los planes pueden agregar fondos desde **Facturación → Saldo prepago** mediante el proveedor de pagos disponible. La ventana de IA muestra el precio aplicable y el saldo prepago disponible antes de generar. Si el saldo no puede cubrir la parte de la solicitud que supera tu cuota, la generación no se inicia y te indica cuánto debes agregar.

Por ejemplo, si quedan dos preguntas incluidas y solicitas cinco, Designer reserva el precio de tres preguntas. Si cuatro candidatos válidos llegan a Review, las dos preguntas incluidas se contabilizan primero, solo se cobran dos preguntas del saldo prepago y la reserva no utilizada de una pregunta se devuelve al saldo prepago.

!!! info "Solo cuentan los candidatos válidos y respaldados por fuentes que llegan a Review"
    Las solicitudes fallidas, los candidatos no válidos, los candidatos sin pruebas de origen verificables y los duplicados rechazados antes de Review no consumen la cuota ni el saldo prepago.

## Fuentes compatibles

Puedes generar a partir del pasaje o estudio de caso actual, seleccionar hasta 10 recursos guardados de la organización o cargar cualquiera de estos tipos de archivo:

- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)
- texto plano en UTF-8 (`.txt`)
- Markdown (`.md` o `.markdown`)
- HTML (`.html` o `.htm`)
- imágenes PNG, JPEG, GIF o WebP

Las fuentes en PDF deben contener texto seleccionable. Ejecuta un OCR antes de cargar un PDF escaneado o que solo contenga imágenes. No se admiten archivos de Office habilitados para macros ni cifrados. Designer lee el código HTML como texto inerte: no ejecuta scripts, no envía formularios, no carga objetos incrustados ni recupera recursos remotos.

Los recursos cargados permanecen en la biblioteca de fuentes privada de tu organización hasta que un usuario los elimine. Si vuelves a cargar el mismo archivo, se reutiliza el recurso existente en lugar de almacenar otra copia.

## Genera candidatos a preguntas

1. Abre un proyecto de examen y selecciona la prueba que debe recibir las preguntas.
2. Selecciona **Redactar preguntas desde tus fuentes** en la barra de herramientas de Exam Explorer.
3. En **Fuente**, elige el pasaje actual, selecciona recursos guardados o carga un archivo compatible. Espera a que cada recurso seleccionado esté listo.
4. En **Preguntas**, agrega una o más filas del plan de diseño.
5. Para cada fila, elige la cantidad exacta, el tipo de pregunta, la dificultad, la puntuación y, de manera opcional, el tema o el resultado de aprendizaje.
6. Selecciona **Generar candidatos**.

Designer admite estos tipos de preguntas generadas:

- Opción múltiple — selección única
- Opción múltiple — selección múltiple
- Completar el espacio en blanco

Las fuentes extensas utilizan una selección enfocada de secciones originales de la fuente en lugar de un resumen de IA. Para mantener económicas las solicitudes a escala de libros completos, Designer requiere al menos tres preguntas solicitadas cuando las fuentes seleccionadas contienen entre 100,000 y 499,999 tokens estimados, y al menos cinco cuando tienen 500,000 tokens o más. Las fuentes más cortas pueden generar una pregunta.

## Revisa antes de insertar

En **Review**, revisa y edita lo siguiente de cada candidato:

- el texto de la pregunta;
- las opciones de respuesta o las respuestas válidas para completar;
- la selección de la respuesta correcta;
- la explicación;
- la dificultad y la puntuación; y
- la cita de la fuente.

Desmarca **Aceptar** o elige **Descartar** para cualquier candidato que no desees. Selecciona **Insertar seleccionadas** solo después de que las preguntas restantes estén listas para la edición y vista previa normales en Designer.

!!! important
    El contenido generado por IA puede ser incompleto, ambiguo o incorrecto incluso cuando cita una fuente. Un experto en la materia debe verificar la redacción, la clave de respuestas, la explicación, la dificultad, la accesibilidad y la puntuación antes de la aplicación del examen.

## Verificación de pruebas y duplicados

Los candidatos deben citar texto que se encuentre en la página de PDF, la sección de Word, la diapositiva de PowerPoint, el rango de líneas de texto, el encabezado de Markdown o el encabezado de HTML indicados antes de poder llegar a Review.

La detección de duplicados compara los candidatos con:

- otros candidatos de la generación actual; y
- preguntas que ya se encuentran en la prueba abierta actualmente.

Designer deliberadamente no compara preguntas de otras pruebas, exámenes o contenido de la organización.

## Si la generación no se completa

- Confirma que el archivo sea de un tipo compatible y contenga suficiente texto legible.
- En el caso de texto, Markdown y HTML, guarda el archivo como UTF-8.
- En el caso de PDF, ejecuta un OCR si no puedes seleccionar y copiar su texto.
- Confirma que la cantidad de preguntas solicitada cumpla con el mínimo para fuentes extensas.
- Selecciona menos fuentes o fuentes más enfocadas e inténtalo de nuevo.
- Verifica la cuota incluida restante y el saldo prepago de la organización.
- Si la cuota se agota, abre **Facturación → Saldo prepago** y agrega al menos el monto faltante que se muestra en la ventana de creación con IA.

Después de la inserción, usa la [vista previa y control de calidad de preguntas](questions.md#preview-and-quality-check) habituales antes de guardar y exportar el proyecto.

## Crea preguntas que utilicen elementos visuales

Cuando una fuente seleccionada contiene una imagen compatible, cada fila del plan de diseño ofrece estas opciones visuales:

| Opción | Qué hace Designer | Uso de preguntas incluidas |
| --- | --- | ---: |
| Sin elemento visual | Genera una pregunta de solo texto. | 1 |
| Reutilizar imagen de la fuente | Usa una imagen relevante extraída de la ubicación de la fuente citada. | 1 |
| Generar nuevo elemento visual | Crea un elemento visual distinto en 1K que evalúa un concepto similar. | 4 |
| Automático | Elige texto, reutilización de la fuente o un nuevo elemento visual según la fuente y devuelve las preguntas reservadas no utilizadas tras la liquidación. | 1 o 4 |

Una pregunta con elementos visuales debe citar texto de origen legible de la misma página de PDF, diapositiva de PowerPoint, sección de documento u otra ubicación de origen que su imagen de referencia. Designer evita portadas, logotipos, imágenes decorativas y secciones preliminares no relacionadas. Los elementos visuales recién generados conservan el historial de su fuente, modelo y trabajo, y permanecen pendientes de revisión humana.

Antes de insertar un candidato con elementos visuales, verifica que la imagen sea relevante, no revele la respuesta y cuente con un texto alternativo preciso y una descripción larga útil. Una imagen fallida o rechazada no consume la cuota de la organización ni el saldo prepago.
