---
title: "Crea y configura una prueba de examen"
description: "Configura el título, instrucciones, duración, secciones, aleatorización, selección de preguntas, calculadora y puntaje de la prueba en Designer."
tags: [designer, exam paper, question bank, sections]
translation_source: user-guides/designer/paper.md
translation_source_sha256: 307977844c66c2b373aa10eafdfcf80aba0eabf5a946b9051fca03824cdf292a
---

# Crea y configura una prueba de examen

Una prueba es una unidad con tiempo medido dentro de un examen. Puede representar una materia, curso, módulo u otro segmento de evaluación. Un examen puede contener varias pruebas.

## Crea una prueba

1. Crea o abre un proyecto de examen.
2. Haz clic derecho en el examen dentro del **Explorador de exámenes**.
3. Selecciona **Nueva prueba de examen**.
4. Selecciona la nueva prueba, como **Prueba 1**.
5. Completa sus propiedades.

Los títulos de las pruebas deben ser únicos dentro del examen.

![Una prueba seleccionada en el Explorador de exámenes, con sus preguntas enumeradas debajo](../../assets/images/designer/paper-in-explorer.png)

## Propiedades de la prueba

**Título de la prueba**

: El nombre visible para el candidato, como Matemáticas, Aptitud o Biología 201.

**Descripción e instrucción**

: Opcional a menos que la opción **Mostrar descripción e instrucción antes de comenzar la prueba** esté activada. Explica las reglas de tiempo, selección, calculadora o navegación específicas de la prueba.

**Duración de la prueba**

: El tiempo permitido en minutos. La duración mínima es de cinco minutos.

**Disposición de las secciones**

: Controla si las secciones se presentan de forma secuencial o si se seleccionan en un orden aleatorio.

**Preguntas por responder**

: Establece cuántas preguntas presenta Client a partir del grupo disponible. Utiliza esto para extraer un subconjunto aleatorio de un banco de preguntas más grande.

Define el valor de preguntas por responder una vez finalizada la creación del contenido. Agregar preguntas más adelante puede restablecer este valor al total de preguntas de la prueba, por lo que debes verificarlo nuevamente antes de exportar.

**Tipo de calculadora**

: Permite elegir entre sin calculadora o una de las calculadoras compatibles: Simple, Avanzada o Base.

**Mostrar puntaje de las preguntas**

: Controla si el puntaje asignado a cada pregunta es visible para el candidato.

## Secciones y contenido

Abre **Contenidos y secciones** para crear secciones y definir:

- el orden de las secciones;
- preguntas secuenciales o aleatorias dentro de una sección; y
- cuántas preguntas se seleccionan de cada sección.

Por ejemplo, una prueba de idioma puede contener las secciones Oral, Comprensión y Vocabulario en un orden fijo, mientras se aleatorizan las preguntas dentro de cada sección.

## Reutiliza preguntas

Para duplicar contenido existente en el proyecto abierto, copia una pregunta y pégala en la prueba de destino. Consulta [Reutilizar contenido del proyecto](importing-questions.md) para conocer el flujo de trabajo compatible. Para importar preguntas desde un documento u otro proyecto, haz clic derecho en la prueba y consulta [Importar contenido existente](import-content.md).

## Valida la prueba

- El título es único y reconocible.
- La duración y las instrucciones coinciden.
- El orden de las secciones y la aleatorización son intencionados.
- La cantidad de preguntas por responder no supera el grupo disponible.
- La configuración de la calculadora y la visualización del puntaje son adecuadas.
- Se ha previsualizado cada una de las preguntas.

Continúa con [Creación de preguntas](questions.md).
