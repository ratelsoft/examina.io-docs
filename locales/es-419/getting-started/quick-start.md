---
title: "Inicio rápido de examina.io"
description: "Configura tu organización, crea o importa un examen, añade candidatos, asigna evaluaciones y publica tu primer examen con examina.io."
tags: [exam setup, getting started, online assessment, quick start]
translation_source: getting-started/quick-start.md
translation_source_sha256: 535b1a2e6b873d0f6b729817ca3c9e64db7b8931167422d03e8816351d9da894
---

# Inicio rápido: publica tu primer examen

Este listado de verificación guía a un administrador de la organización desde una cuenta nueva hasta un enlace de examen listo para probar. Si otra persona redacta las preguntas, puede completar los pasos en Designer y enviarte el archivo `.smex` exportado.

## 1. Confirma el acceso del personal

Desde **Inicio**, verifica que las personas que preparan la evaluación tengan los [roles de cuenta](roles-and-permissions.md) correctos. Usa **Usuarios** para añadir cuentas de personal y **Círculos** si el acceso debe limitarse a exámenes o candidatos particulares.

![La galería de aplicaciones de examina.io después de iniciar sesión](../assets/images/dashboard/apps-gallery.png)

## 2. Crea el contenido del examen

Abre **Designer** y luego:

1. Selecciona **Archivo → Nuevo proyecto de examen**.
2. Crea un examen y al menos una prueba.
3. Añade secciones y preguntas.
4. Define las instrucciones del examen y de la prueba, la duración, la puntuación y las reglas de navegación.
5. Previsualiza el contenido.
6. Exporta el examen finalizado como un archivo `.smex`.

Para obtener instrucciones detalladas sobre la creación de contenido, consulta [Presentación de Designer](../user-guides/designer/introduction.md).

## 3. Importa el examen en Manager

Abre **Manager** y elige **Archivo → Añadir nuevo examen**. Selecciona el archivo `.smex` exportado y espera el mensaje de confirmación. Revisa el título, código, pruebas y propiedades de envío importados antes de asignarlo a nadie.

Consulta [Importar exámenes](../user-guides/manager/import-exams.md).

## 4. Añade candidatos

Elige uno de estos métodos:

- **Archivo → Añadir nuevo candidato** para una o pocas personas.
- **Archivo → Importar candidatos desde archivo/Excel** para una clase o grupo.

Un candidato es la persona que rinde un examen, no un usuario del personal. Mantén su código o ID único. Si importas un archivo, verifica la asignación de campos y previsualiza antes de comenzar la importación.

Consulta [Añadir e importar candidatos](../user-guides/manager/examinees.md).

## 5. Crea Grupos cuando sea útil

Los Grupos son opcionales, pero reducen el trabajo repetitivo. Crea un Grupo para una clase, cohorte, departamento o sesión, y luego añade a los candidatos correspondientes.

Puedes asignar un Grupo completo a un examen y, al mismo tiempo, seleccionar las pruebas y la hora de inicio opcional para esa asignación.

## 6. Asigna el examen y las pruebas

Selecciona un examen y elige **Asignar candidatos** o **Asignar grupos**. Mueve a las personas o Grupos deseados a la lista seleccionada, continúa con la asignación de pruebas y elige las pruebas que pueden rendir.

Si configuras una hora para el examen, selecciona también la zona horaria correcta. La hora asignada es el momento más temprano en que el examen estará disponible para esa asignación.

## 7. Configura el envío

Antes de compartir el enlace, revisa:

- la visibilidad del examen;
- si los resultados se muestran al finalizar;
- los requisitos de supervisión de exámenes en vivo y verificación de identidad;
- el acceso permitido desde celular o tableta;
- el comportamiento ante la desconexión de internet; y
- cualquier exención de supervisión de exámenes.

Mantén el examen invisible mientras lo preparas. Hazlo visible solo cuando el examen y las asignaciones estén listos.

## 8. Prueba la experiencia del candidato

Abre el enlace del examen en una ventana privada del navegador. Confirma que:

- el logo de la organización y el estilo de inicio de sesión sean correctos;
- el candidato de prueba pueda iniciar sesión;
- las pruebas esperadas estén disponibles;
- las instrucciones y los tiempos sean correctos; y
- las verificaciones de dispositivo, cámara, micrófono o identidad funcionen según lo esperado.

Usa un candidato de prueba ficticio o designado en lugar de un candidato real.

## 9. Publica y comunica

Haz visible el examen, luego copia **Abrir enlace del examen** o usa [**Enviar correo electrónico a los candidatos**](../user-guides/manager/email-examinees.md) desde Manager. Incluye:

- la fecha del examen, la hora de inicio y la zona horaria;
- el enlace del examen;
- el método de distribución del código y la contraseña del candidato;
- los requisitos de dispositivo y navegador;
- los requisitos de supervisión de exámenes; y
- un contacto de soporte.

Comparte la [guía para el candidato en el día del examen](../user-guides/client/take-an-exam.md) con los participantes.

## 10. Monitorea y genera informes

Durante la sesión, actualiza Manager para ver los estados de conexión actuales. Si la supervisión de exámenes en vivo está habilitada, abre el examen en **Proctoring**. Después de que los candidatos terminen, revisa los resultados individuales o genera un informe del examen.

La [guía de envío, monitoreo e informes](../user-guides/manager/deliver-monitor-report.md) contiene la lista de verificación operativa detallada.

!!! tip "Realiza un ensayo"
    Para una evaluación de alto impacto, realiza un breve ensayo con las mismas reglas de dispositivos, condiciones de red y configuración de supervisión de exámenes planificadas para el examen real.
