---
title: "Introducción a examina.io Designer"
description: "Conoce el espacio de trabajo de Designer y crea un proyecto de examen, cuadernillos, secciones y preguntas para su entrega en examina.io."
tags: [assessment authoring, designer, exam project, questions]
translation_source: user-guides/designer/introduction.md
translation_source_sha256: 00ffb0a122c3a4edb7cc94fbec1d25afdddeaa592ab5240604581e63c4551fbb
---

# Introducción a Designer

Designer es el lugar donde se redactan los exámenes. Creas un **proyecto**, incluyes uno o más **exámenes** en él, divides cada examen en **cuadernillos** y llenas los cuadernillos con **preguntas**. Cuando el examen esté listo, envíalo a Manager, que es donde se asigna a las personas y se aplica.

Designer se ejecuta en el navegador y no requiere instalar nada.

![El espacio de trabajo de Designer sin ningún proyecto abierto](../../assets/images/designer/workspace-empty.png)

## El espacio de trabajo

Cuatro áreas que se mantienen siempre en el mismo lugar.

| Área | Lo que contiene |
|---|---|
| **Exam Explorer** (arriba a la izquierda) | El árbol del proyecto: exámenes, luego cuadernillos y después preguntas |
| **Properties** (abajo a la izquierda) | La configuración de lo que esté seleccionado en el árbol |
| **Hint** (abajo a la izquierda) | Explicación sencilla de la propiedad seleccionada |
| **Panel de edición** (derecha) | El examen, cuadernillo o pregunta en el que estás trabajando |

Vale la pena conocer el panel Hint. Selecciona cualquier fila en Properties y te explicará qué hace esa configuración, lo cual suele ser más rápido que buscarlo.

## Dos tipos de archivo

Esta distinción causa más confusión que cualquier otra cosa en Designer, por lo que conviene tenerla clara antes de comenzar.

| Archivo | Extensión | Qué es |
|---|---|---|
| **Proyecto** | `.smexproj` | Tu archivo fuente editable. Contiene cada examen, cuadernillo y pregunta, y se puede volver a abrir y modificar |
| **Examen** | `.smex` | Un solo examen empaquetado para su aplicación. Esto es lo que utiliza Manager |

Conserva el proyecto. Si lo pierdes y solo te quedas con el examen exportado, perderás la capacidad de editarlo fácilmente.

## Crear un proyecto

1. Elige **Archivo → Nuevo proyecto de examen**.
2. Designer creará un **Examen sin título** en su interior.
3. Selecciona ese examen en Exam Explorer para completar sus detalles.
4. Elige **Archivo → Guardar proyecto** y guarda el archivo `.smexproj` en un lugar seguro.

![El menú Archivo](../../assets/images/designer/file-menu.png)

Observa qué elementos están desactivados en gris y cómo se activan en dos etapas. **Guardar proyecto**, **Guardar proyecto como...** y **Nuevo examen** estarán disponibles una vez que haya un proyecto abierto. Las dos acciones de exportación permanecerán deshabilitadas hasta que **selecciones un examen** en Exam Explorer, ya que Designer exporta un examen a la vez y necesita saber cuál. Que el menú Archivo esté lleno de texto en gris no es un error: por lo general, significa que aún no has seleccionado nada.

## Abrir un proyecto existente

**Archivo → Abrir proyecto**, luego elige un archivo `.smexproj`.

!!! warning "Los proyectos de una versión más reciente no se abrirán"
    Designer rechaza los proyectos guardados con una versión posterior de la aplicación a la que estás ejecutando, ya que no puede garantizar que comprenderá todo su contenido. Verás el mensaje *"The file version is greater than the application version"*.

    Exporta el examen desde la versión que lo creó o pídele a quien te lo envió que lo guarde desde una versión compatible.

![El proyecto de muestra abierto con su examen en Exam Explorer](../../assets/images/designer/project-loaded.png)

Las capturas de pantalla de estas páginas utilizan un solo ejemplo de referencia: un proyecto llamado **Northgate Entrance Exam 2026** que contiene un único examen, *Northgate Entrance Examination*, dividido en seis cuadernillos.

## La estructura de un examen

Todo en Designer se anida de la misma manera:

```
Project
└── Exam                     uno o más
    └── Paper                uno o más
        └── Question         una o más
            └── Section      agrupación opcional dentro de un cuadernillo
```

Un **cuadernillo** suele corresponder a una materia, curso o módulo. Un examen con seis cuadernillos puede ser una sola sesión que abarque seis materias, con su propia duración y conjunto de preguntas para cada una.

## Añadir un cuadernillo

Haz clic derecho sobre el examen en Exam Explorer y elige **Nuevo cuadernillo de examen**, luego selecciona el nuevo cuadernillo para configurar su título, duración e instrucciones. Consulta [El cuadernillo](paper.md) para saber qué hace cada configuración.

## Añadir una pregunta

Haz clic derecho en un cuadernillo y elige la acción para crear una nueva pregunta, o bien usa el botón ubicado debajo de Exam Explorer. Designer es compatible con:

- Opción múltiple con respuesta única
- Opción múltiple con respuestas múltiples
- Completar el espacio en blanco

Define la respuesta, la puntuación y la sección; luego, usa **Vista previa** para ver la pregunta exactamente como la verá el candidato. Consulta [Creación de preguntas](questions.md).

## Un flujo de trabajo recomendado

1. Configura el [examen](exam.md): título, código, descripción e instrucciones
2. Crea cada [cuadernillo](paper.md) y define su duración
3. Añade secciones si el cuadernillo las necesita
4. Escribe las [preguntas](questions.md) o [impórtalas](import-content.md)
5. Genera una vista previa y revisa el contenido
6. **Guarda el proyecto**
7. Exporta un examen a [Manager](../manager/import-exams.md)

También puedes [reutilizar cuadernillos y preguntas](importing-questions.md) de cualquier otra parte del proyecto abierto, [importar contenido existente](import-content.md) desde otro proyecto o documento, o crear borradores a partir de tus propias fuentes con la [creación mediante IA](ai-question-authoring.md).
