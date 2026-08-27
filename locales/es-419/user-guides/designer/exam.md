---
title: "El examen"
description: "Configura el título del examen, el código, la marca, la descripción, las instrucciones, el flujo de secciones y la visibilidad de respuestas en examina.io Designer."
tags: [designer, exam settings, exam code, branding, paper flow]
translation_source: user-guides/designer/exam.md
translation_source_sha256: 08c940d21a9db0e95244f721e5db54146dfe7c47b7d4b9ec56cc739ca87bf2d8
---

# El examen

Selecciona un examen en Exam Explorer y el panel de edición mostrará todo lo que se aplica al examen en su totalidad. La mayor parte es visible para el candidato, por lo que vale la pena hacerlo a conciencia en lugar de completarlo solo para pasar de pantalla.

![Propiedades y configuración del examen](../../assets/images/designer/exam-properties.png)

## Título del examen

El nombre que ve el candidato mientras realiza el examen. Escríbelo como lo imprimirías en papel: *Northgate Entrance Examination*, no *entrance-final-v2*.

!!! note "Acerca de los ejemplos"
    Las capturas de pantalla de las páginas de Designer utilizan un proyecto de muestra,
    **Northgate Entrance Exam 2026**, que contiene un solo examen llamado
    *Northgate Entrance Examination* con seis secciones. Cuando esta guía mencione el
    valor de un campo, se trata del valor visible en esa muestra.

## Código del examen

**Obligatorio, y el campo que más problemas suele causar más adelante.**

El código identifica al examen cuando llega a Manager, por lo que debe ser único entre todos los exámenes que importe tu organización. Si dos exámenes comparten un código, no se podrán importar correctamente.

Dos reglas que impone este campo:

- **Sin espacios**
- **Solo letras y números**: sin signos de puntuación, guiones ni guiones bajos

`NGCENTRY26` está bien, y es el código utilizado en la muestra. `NGC ENTRY 26` y
`NGC-ENTRY-26` no lo están.

!!! tip "Define un esquema antes de tu segundo examen, no del vigésimo"
    Algo como `SUBJECT` + `YEAR` + `SITTING` se mantiene legible y
    único: `NGCENTRY26`, `NGCMOCK26`. Reestructurar un esquema después implica volver a importar
    exámenes que ya están en uso.

## Banner de marca y color

Opcional. El banner se le muestra al candidato mientras rinde el examen y el color le da un tinte a la interfaz circundante.

Utilízalos cuando una sola organización entregue exámenes en nombre de varios departamentos o clientes, y cada uno deba tener su propia apariencia. **Clear** elimina cualquiera de los dos sin afectar al otro.

## Descripción

Se muestra al candidato antes de comenzar y es lo primero que lee un candidato nervioso. Explica qué **es** el examen y qué **abarca**, con un lenguaje sencillo.

Información útil para incluir aquí:

- para qué sirve el examen: ingreso, fin de módulo, práctica
- qué materias o temas abarca y cuántas secciones tiene
- aproximadamente cuánto dura la sesión completa
- qué significa aprobar, si eso ya está decidido de antemano

La muestra utiliza:

> Seis secciones que abarcan razonamiento cuantitativo, razonamiento verbal, química,
> bioquímica, actualidad y religión.

Evita repetir el título del examen y evita las referencias internas, como números de versión o códigos de comité. El candidato no puede hacer nada con esa información.

## Instrucciones generales

También se muestra antes de que comience el examen. Esto es para las reglas de la sala: cosas que un candidato debe saber para rendir el examen correctamente, aplicables a **todas** las secciones.

Información útil para incluir aquí:

- si deben responder todas las preguntas o si pueden elegir
- si pueden desplazarse entre secciones y si pueden regresar
- qué está permitido: calculadora, notas, hojas de borrador
- qué sucede si se pierde la conexión o se cierra el navegador
- cómo reportar un problema durante el examen
- si el trabajo se va guardando a medida que avanzan

La muestra utiliza:

> Responde todas las preguntas. Puedes desplazarte entre secciones hasta que envíes el examen. Tu trabajo
> se guarda a medida que avanzas.

Esa última oración hace más de lo que parece: los candidatos que no saben que sus respuestas se están guardando evitarán navegar y pasarán el examen con la ansiedad de perder su trabajo.

!!! tip "Explica qué sucede si algo sale mal"
    La instrucción que más vale la pena incluir es la que nadie escribe: qué hacer si
    se pierde la conexión. Un candidato que sabe que puede volver a conectarse lo hará.
    Quien no lo sepa, puede darse por vencido.

Las instrucciones específicas de cada sección pertenecen a [la sección](paper.md): la duración, la selección de preguntas y todo lo que se aplique a una sola materia. Cualquier otra cosa que de otro modo repetirías en cada sección pertenece aquí.

## Flujo de secciones del examen

Para exámenes con más de una sección, esto determina cómo aparece la siguiente sección.

| Configuración | Comportamiento |
|---|---|
| **Server Controlled** | El servidor decide cuándo se abre cada sección. Todos avanzan al mismo tiempo |
| **Client Controlled** | El candidato avanza cuando finaliza la sección actual |
| **Force Continuous** | Las secciones se ejecutan una tras otra sin pausas |

Elige **Server Controlled** para una sesión en la que todos deban estar en la misma sección al mismo tiempo. Elige **Client Controlled** cuando los candidatos deban trabajar a su propio ritmo dentro de un límite de tiempo global.

## Mostrar respuestas al finalizar el examen

Determina si el candidato ve cuáles respuestas fueron correctas una vez que envía el examen.

Útil para exámenes de práctica y repaso. Casi siempre es un error para una evaluación en vivo, porque les entrega la clave de respuestas a quienes rinden temprano.

## Permitir navegación entre secciones

Determina si un candidato puede regresar a una sección que ya abandonó.

Configúralo en **No** cuando cada sección deba quedar sellada una vez enviada. Configúralo en **Yes** cuando todo el examen sea realmente una sola prueba larga dividida en partes y los candidatos deban tener la libertad de volver a revisarla.

## Antes de continuar

El código del examen es la única configuración que resulta realmente problemática de cambiar más adelante, porque es la forma en que Manager reconoce el examen. Todo lo demás se puede editar y volver a exportar sin consecuencias.

A continuación: [La sección](paper.md).
