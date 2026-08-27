---
title: "Descripción general de la plataforma examina.io"
description: "Comprende cómo Designer, Manager, Proctor, Client, usuarios, grupos y Circles trabajan juntos en la evaluación de examina.io."
tags: [assessment platform, client, designer, examinees, exams, manager, proctoring]
translation_source: getting-started/overview.md
translation_source_sha256: 3758552e04cfd298de85e07c2a290dd7c4675706cab28137e1fb9cf0b0dae7ca
---

# Comprende la plataforma examina.io

examina.io separa el trabajo de evaluación en aplicaciones enfocadas. Los autores de preguntas pueden crear contenido sin acceso a los registros de los candidatos, los administradores pueden programar y realizar exámenes, los supervisores solo pueden supervisar los exámenes que tienen asignados y los candidatos usan una aplicación Client dedicada.

![La galería de aplicaciones de examina.io muestra Designer, Manager y Client](../assets/images/dashboard/apps-gallery.png)

## Flujo de trabajo de evaluación

1. **Crea** un proyecto de examen, pruebas, secciones y preguntas en Designer.
2. **Exporta** el examen completado como un archivo `.smex`.
3. **Importa** ese archivo en Manager.
4. **Agrega candidatos** de forma individual o impórtalos desde Excel, CSV o texto.
5. **Organiza y asigna** candidatos con Groups, asignaciones de exámenes y asignaciones de pruebas.
6. **Configura las opciones** de entrega, como visibilidad, hora de inicio, visualización de resultados, dispositivos compatibles, verificación de identidad y supervisión en vivo.
7. **Comparte el enlace del examen** o envía un correo electrónico desde Manager.
8. **Monitorea y genera informes** mientras el examen esté activo y después de que finalice.

La misma persona puede realizar varias etapas en una organización pequeña. Las organizaciones más grandes pueden separar las responsabilidades con [roles de cuenta y Circles](roles-and-permissions.md).

## Designer

Designer es la aplicación para la creación de exámenes. Úsala para crear proyectos de examen, organizar una o más pruebas, agregar secciones, redactar preguntas, establecer reglas de puntuación y tiempo e importar contenido de preguntas existente.

![La misma pregunta en el panel de edición y en el panel de vista previa de Designer](../assets/images/general/designer-edit-preview.png)

Cuando finalices la creación, exporta el examen como un archivo `.smex` encriptado para su entrega a través de Manager. Comienza con [Introducción a Designer](../user-guides/designer/introduction.md).

## Manager

Manager conecta el contenido del examen con las personas que lo rinden. Los administradores y el personal autorizado usan Manager para:

- importar archivos de examen `.smex`;
- crear o importar registros de candidatos;
- organizar candidatos en Groups;
- vincular candidatos o Groups a un examen y sus pruebas;
- controlar la visibilidad del examen y las opciones de entrega;
- abrir o distribuir un enlace de examen; y
- monitorear el progreso y generar resultados u informes.

![Un examen en Manager con sus candidatos vinculados](../assets/images/manager/exam-details.png)

Consulta la [descripción general de Manager](../user-guides/manager/overview.md) para conocer la navegación principal y la secuencia operativa recomendada.

## Proctor

Proctor es el espacio de trabajo de supervisión en vivo. Cuando la supervisión en vivo está habilitada para un examen, los supervisores autorizados pueden revisar la transmisión disponible de audio, cámara web y pantalla, comunicarse con un candidato y aprobar el inicio de un examen cuando el flujo de trabajo configurado lo requiera.

![El espacio de trabajo de Proctor, una tarjeta por candidato](../assets/images/general/proctoring-view.png)

Cada candidato conectado aparece como una tarjeta con vistas de Detalles, Cámara web y Pantalla, controles de grabación y silencio, y una casilla de mensajes directos.

Solo habilita las funciones de supervisión de exámenes que tu organización esté autorizada a usar e informa a los candidatos sobre los datos que se recopilarán.

## Client

Client es la aplicación orientada al candidato. Los candidatos abren el enlace del examen, ingresan sus credenciales asignadas, completan cualquier verificación de sistema o de identidad requerida y rinden las pruebas vinculadas.

![La aplicación Client orientada al candidato](../assets/images/client/question.png)

Client guarda de forma periódica el estado del examen mientras haya una conexión disponible. La [guía para el día de la prueba](../user-guides/client/take-an-exam.md) explica cómo deben prepararse los candidatos y qué hacer si se interrumpe la conexión.

## Users, Groups, and Circles

Estos conceptos de apariencia similar resuelven problemas diferentes:

| Concepto | Propósito |
| --- | --- |
| **Usuario** | Una cuenta de personal que inicia sesión en examina.io, como un administrador, coordinador de exámenes o supervisor. |
| **Candidato** | Un candidato o estudiante que inicia sesión a través de un enlace de examen para rendir una evaluación. |
| **Group** | Una colección reutilizable de candidatos, utilizada para la asignación masiva de exámenes y pruebas. |
| **Circle** | Un límite de permisos que conecta usuarios seleccionados con exámenes y candidatos seleccionados. |

Usa Groups para reducir el trabajo de asignación repetitivo. Usa Circles para restringir lo que el personal puede ver y administrar. Obtén más información en [Groups y asignaciones de exámenes](../user-guides/manager/groups-and-assignments.md) y [Circles y permisos](../user-guides/administration/circles-and-permissions.md).

## Integraciones

Las organizaciones pueden conectar examina.io a otros sistemas mediante:

- claves API públicas y secretas;
- un webhook de finalización;
- el widget incrustable de Client;
- la API REST; y
- integraciones de plataformas de aprendizaje compatibles que se muestran en Configuración.

Comienza con [Claves API y webhooks](../integrations/api-keys-and-webhooks.md) o ve directamente a la [Referencia de la API](../api/index.md).

## Siguiente paso

Sigue la [guía de inicio rápido](quick-start.md) para obtener una lista de verificación práctica para tu primer examen.
