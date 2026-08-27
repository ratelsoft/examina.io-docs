---
title: "Integra examina.io con Canvas mediante LTI 1.3"
description: "Conecta Canvas a examina.io, elige evaluaciones publicadas con LTI Deep Linking, inícialas en un curso y devuelve calificaciones con Assignment and Grade Services."
tags: [Canvas LMS, LTI 1.3, LMS integration, Deep Linking, AGS, NRPS, gradebook]
translation_source: integrations/canvas-lms.md
translation_source_sha256: a00b087c1df6149f09f18bf711a3a543691d492ce5a776d673d31fdcb8922f30
---

# Integra examina.io con Canvas

Conecta examina.io a una cuenta raíz de Canvas y luego permite que los profesores agreguen
evaluaciones publicadas a las tareas sin copiar enlaces de exámenes. Los estudiantes abren la
evaluación dentro de Canvas sin tener que iniciar sesión por segunda vez, y examina.io devuelve cada
resultado a la columna correspondiente del libro de calificaciones de Canvas.

!!! tip "Valida antes de una evaluación en vivo"

    Conecta y valida el flujo de trabajo completo en un curso de Canvas que no sea de producción
    con usuarios ficticios antes de habilitarlo para una evaluación en vivo.

Las capturas de pantalla utilizan un curso ficticio de **Northbridge College**,
**Introduction to Biology (BIO 101)**, y una evaluación llamada **Cell
Structure and Function**. Tu institución, el nombre de host de Canvas, los identificadores y
los nombres de los cursos serán diferentes.

## Lo que ofrece la integración

- **Un solo inicio de sesión en Canvas:** los estudiantes no vuelven a iniciar sesión en examina.io cuando
  abren una tarea desde Canvas.
- **Selección de evaluaciones publicadas:** LTI Deep Linking permite que el profesor elija
  el examen exacto mientras crea una tarea de Herramienta externa.
- **Ubicación contextualizada al curso:** la publicación seleccionada queda vinculada al curso y a la
  tarea de Canvas que la crearon.
- **Devolución de calificaciones:** LTI Assignment and Grade Services (AGS) envía la puntuación al
  estudiante y a la columna del libro de calificaciones correctos.
- **Lista de curso opcional:** Names and Roles Provisioning Services (NRPS) puede
  proporcionar los datos mínimos de membresía del curso requeridos por un flujo de trabajo aprobado.

Canvas llama a este patrón una ubicación `assignment_selection`. Su documentación
oficial confirma que la ubicación utiliza Deep Linking, carga la evaluación de la
herramienta elegida para los estudiantes asignados y puede sincronizar calificaciones a través de los servicios de calificación de LTI.

## Antes de comenzar

Necesitas:

- una cuenta Root o Administrator en examina.io;
- un administrador de la cuenta raíz de Canvas que pueda gestionar Developer Keys y Apps;
- un instructor y un estudiante ficticio en un curso de Canvas que no sea de producción;
- al menos un examen importado y publicado en examina.io Manager;
- direcciones HTTPS públicas con certificados de confianza para ambos sistemas; y
- un plan aprobado por la institución para los datos de los estudiantes que Canvas pueda divulgar.

Mantén precisos los relojes de ambos sistemas. Los mensajes de inicio de sesión de LTI y las respuestas firmadas
expiran rápidamente, por lo que una gran diferencia de hora puede rechazar una configuración que por lo demás sería correcta.

## Cómo intercambian configuraciones Canvas y examina.io

Canvas crea un **Client ID** y un **Deployment ID** que examina.io necesita.
examina.io crea una URL de clave pública específica del registro que Canvas necesita.
Por lo tanto, durante la vista previa, la configuración consta de dos pasos:

1. crea una Developer Key provisional de Canvas LTI 1.3 e instala su App;
2. copia los identificadores de Canvas y los endpoints de la plataforma en examina.io;
3. copia los endpoints finales de examina.io de vuelta en la clave de Canvas; y
4. enciende la App, hazla disponible y valida el flujo de trabajo completo.

!!! warning "Mantén la App provisional no disponible"

    Si Canvas requiere una URL de clave pública durante la primera pasada, usa un endpoint HTTPS JSON Web Key Set
    temporal controlado por tu institución. Puede devolver un conjunto vacío (`{"keys":[]}`). Mantén la clave desactivada y la App
    no disponible hasta que la reemplaces con la URL del **Public key set (JWKS)** específica del registro de
    examina.io en el Paso 3. Nunca uses un nombre de host local, Docker o privado
    en una clave de producción de Canvas.

## 1. Crea la clave y la App provisionales de Canvas

Inicia sesión con una cuenta de administrador de la cuenta raíz de Canvas. Selecciona **Admin** en
la navegación global y luego elige la cuenta raíz de tu institución. Si Canvas
muestra primero la lista de cuentas, selecciona el nombre de la cuenta raíz.

![Seleccionar la cuenta raíz de Canvas de la institución](../assets/images/integrations/canvas/admin-01-accounts.png)

La navegación de la cuenta debe incluir **Developer keys** y **Apps**. Si falta
alguno de los elementos, tu rol de Canvas no tiene el permiso de cuenta raíz requerido; pide al administrador de Canvas de la institución que realice esta configuración.

![Abrir Developer keys desde la navegación de la cuenta raíz de Canvas](../assets/images/integrations/canvas/admin-02-root-account.png)

Abre **Developer keys** y luego selecciona **+ Developer Key**.

![Abrir la página de Developer keys de Canvas](../assets/images/integrations/canvas/admin-03-developer-keys.png)

Elige **LTI Key**. Canvas también puede mostrar **LTI Registration**; usa esa opción
solo cuando examina.io haya proporcionado una URL de Dynamic Registration de un solo uso.

![Elegir LTI Key del menú Developer Key de Canvas](../assets/images/integrations/canvas/admin-04-create-lti-key.png)

Elige **Manual Entry** y luego completa la configuración de la clave:

1. Ingresa **examina.io Assessments** como nombre y título de la clave.
2. Agrega la dirección de correo electrónico del administrador responsable de esta
   integración.
3. Agrega `https://www.examina.io/lti/launch` y
   `https://www.examina.io/lti/deep-link` como URIs de redirección separadas.
4. Ingresa `https://www.examina.io/lti/launch` como la **Target Link URI**.
5. Ingresa `https://www.examina.io/lti/login` como la **OpenID Connect
   Initiation URL**.
6. Establece **JWK Method** en **Public JWK URL** e ingresa la URL del conjunto de claves
   provisional descrita anteriormente.

![Ingresar las URLs públicas de examina.io en una clave LTI de Canvas](../assets/images/integrations/canvas/admin-05-lti-key-settings.png)

!!! warning "El valor de JWKS es específico del registro"

    Si usas `https://www.examina.io/lti/jwks/your-registration-id` durante
    el paso provisional, `your-registration-id` es solo un marcador de posición. El Paso
    3 reemplaza todo el valor con la URL exacta del **Public key set (JWKS)**
    que muestra examina.io.

En **LTI Advantage Services**, habilita únicamente los cinco alcances necesarios para los
servicios de esta guía:

- crear y ver datos de tareas;
- ver datos de tareas;
- ver datos de entregas;
- crear y actualizar resultados de entregas; y
- recuperar datos de usuario asociados con el contexto.

Los primeros cuatro respaldan la devolución de calificaciones a través de AGS. El alcance final respalda la
lista de curso opcional de NRPS; déjalo deshabilitado cuando no necesites acceso a la lista.

![Seleccionar los alcances de AGS de Canvas y NRPS opcionales](../assets/images/integrations/canvas/admin-06-lti-services.png)

En **Placements**, agrega **Assignment Selection**. Agrega **Course Navigation**
solo si tu institución también desea un punto de entrada a nivel de curso para examina.io.

![Agregar ubicaciones de Assignment Selection y Course Navigation opcional](../assets/images/integrations/canvas/admin-07-placements.png)

Guarda la clave, copia su **Client ID** y mantén la clave en **Off**. Abre **Admin →
tu cuenta raíz → Apps → Manage**, instala la App usando el Client ID y
copia su **Deployment ID**.

Canvas también admite Dynamic Registration, pero sus APIs de registro están
actualmente marcadas como beta. Usa una URL de Dynamic Registration de un solo uso solo cuando examina.io la haya proporcionado explícitamente para tu vista previa; de lo contrario, usa el flujo manual de dos pasos anterior.

## 2. Agrega el registro de Canvas en examina.io

Como Root o Administrator en examina.io:

1. Abre **Home → Settings**.
2. Busca **Bring Examina into your LMS** y selecciona **Add registration**.
3. Elige **Canvas** e ingresa un nombre descriptivo, como **Northbridge
   College Canvas**.
4. Ingresa los valores de Canvas que se muestran a continuación.

| Campo de examina.io | Valor de Canvas |
| --- | --- |
| Issuer URL | `https://<your-canvas-host>` |
| Client ID | El Client ID de la Developer Key de LTI |
| Deployment ID | El Deployment ID de la App instalada |
| Authorization endpoint | `https://<your-canvas-host>/api/lti/authorize_redirect` |
| Token endpoint | `https://<your-canvas-host>/login/oauth2/token` |
| LMS public keys (JWKS) URL | `https://<your-canvas-host>/api/lti/security/jwks` |

Para un Canvas alojado, reemplaza `<your-canvas-host>` con el nombre de host exacto en el que tus
usuarios inician sesión. No agregues una ruta final al Issuer URL y no uses el endpoint genérico OAuth JWKS de Canvas en el campo de claves públicas del LMS.

5. Habilita **Assessment selection (Deep Linking)** y **Grade return (AGS)**.
6. Habilita **Course roster (NRPS)** solo si el alcance coincidente de Canvas fue
   aprobado y otorgado.
7. Selecciona **Save registration**.

![Agregar un registro de Canvas LTI 1.3 en examina.io](../assets/images/integrations/canvas/01-examina-add-canvas-registration.png)

La tarjeta guardada muestra las URLs exactas de **OIDC login initiation**, **LTI launch**,
**Deep Linking** y la URL específica del registro de **Public key set (JWKS)**.
Mantén esa tarjeta abierta para el siguiente paso.

## 3. Finaliza y activa la App de Canvas

Edita la Developer Key de LTI de Canvas y reemplaza cada valor provisional de la herramienta
con el valor exacto mostrado por examina.io:

| Campo de clave LTI de Canvas | Valor de examina.io |
| --- | --- |
| OpenID Connect Initiation URL | OIDC login initiation |
| Target Link URI | LTI launch |
| Redirect URI | URLs de LTI launch y Deep Linking, una por línea |
| Assignment Selection target link | Deep Linking |
| Public JWK URL | Public key set (JWKS) |
| Tool Icon URL | `https://www.examina.io/img/logo128.png` |

Las rutas de producción orientadas al navegador comienzan con `https://www.examina.io`.
Por ejemplo, la URL de inicio es
`https://www.examina.io/lti/launch`. Copia siempre los valores completos de la
tarjeta de registro porque la URL de JWKS incluye el identificador de registro.

Guarda la clave y enciéndela (**On**). En **Apps → Manage**, abre **examina.io
assessments**, confirma que la App esté encendida y hazla disponible para la cuenta
raíz o para las subcuentas y cursos aprobados.

El **Tool Icon URL** proporciona a los instructores y administradores un logotipo reconocible de
examina.io en Canvas. Si una instalación existente aún muestra el ícono genérico de herramienta externa de Canvas, actualiza la Developer Key con este valor y
actualiza o vuelve a instalar la App para que Canvas recargue sus metadatos de registro.

![Confirmar que examina.io Assessments esté activada y actualizada en Canvas Apps](../assets/images/integrations/canvas/admin-08-apps-manage.png)

Si la App muestra **Not Available**, abre su configuración de disponibilidad, elige la
cuenta raíz o una subcuenta aprobada, selecciona **Available** y guarda. Limita
la disponibilidad a las instituciones, subcuentas o cursos aprobados para la
integración.

![Hacer que la App de Canvas esté disponible para la cuenta aprobada](../assets/images/integrations/canvas/admin-09-availability.png)

Regresa a examina.io y activa el registro. Un registro suspendido o revocado
no puede aceptar nuevos inicios.

## 4. Agrega una evaluación publicada a una tarea de Canvas

Como instructor en el curso de destino:

1. Abre **Assignments → + Assignment**.
2. Ingresa el nombre de la tarea orientado al estudiante y el puntaje máximo.
3. Establece **Submission type** en **External tool**.
4. Selecciona **Find** y luego elige **Add an examina.io assessment**.
5. Selecciona el examen publicado deseado y elige **Add selected exam**.

![Elegir una evaluación publicada de examina.io desde Canvas](../assets/images/integrations/canvas/04-canvas-select-published-exam.png)

Canvas regresa al formulario de la tarea con la URL de inicio seleccionada. Confirma
el nombre de la tarea, los puntos, el acceso a la tarea, las fechas y la política de intentos.

![Una tarea de Herramienta externa de Canvas que utiliza la URL de inicio de producción de examina.io](../assets/images/integrations/canvas/05-canvas-assignment-settings.png)

Elige **Save & publish**, luego abre la tarea una vez como instructor.
Confirma que aparezca la evaluación esperada y que Canvas no pida
un inicio de sesión independiente en examina.io.

## 5. Verifica la experiencia del estudiante

Usa un estudiante ficticio inscrito en el curso:

1. Inicia sesión en Canvas como el estudiante.
2. Abre **BIO 101 → Assignments → Cell Structure and Function**.
3. Confirma que el examen esperado se abra dentro de la tarea de Canvas.
4. Comienza, completa y envía la evaluación.

![Una evaluación publicada de examina.io incrustada en una tarea de Canvas](../assets/images/integrations/canvas/06-canvas-learner-assessment.png)

El inicio de LTI verifica la plataforma de Canvas, el despliegue, el curso, la tarea,
el estudiante y la publicación seleccionada. Una URL de inicio copiada no reemplaza
el abrir la tarea desde Canvas.

## 6. Verifica la calificación devuelta

Después de enviar la evaluación, abre la vista de calificaciones de Canvas como estudiante o el libro de calificaciones (Gradebook)
como instructor. Confirma que el resultado aparezca para la tarea y el estudiante correctos.

![La evaluación de examina.io completada enviada de vuelta al libro de calificaciones de Canvas](../assets/images/integrations/canvas/07-canvas-grade-return.png)

La entrega de calificaciones se pone en cola por separado del envío del examen, por lo que una interrupción temporal de
Canvas no convierte una evaluación completada en un envío fallido.
La puntuación puede tardar un poco en aparecer. Actualiza la vista de calificaciones antes de
investigar un resultado faltante.

## Lista de verificación de validación en producción

Antes de habilitar la App para un curso en vivo, verifica todo lo siguiente con un
curso que no sea de producción y usuarios ficticios:

- La clave y la App de Canvas están activadas y disponibles únicamente donde corresponda.
- El registro de examina.io está activo en la organización y el entorno correctos.
- Canvas utiliza la URL de JWKS de examina.io específica del registro.
- examina.io utiliza el endpoint `/api/lti/security/jwks` de Canvas.
- Deep Linking enumera únicamente las evaluaciones que el instructor puede seleccionar.
- La tarea inicia la evaluación publicada prevista dentro de Canvas.
- El estudiante inicia la evaluación sin tener que iniciar sesión por segunda vez.
- La puntuación completada llega al estudiante y a la columna del libro de calificaciones correctos.
- Volver a abrir o actualizar la tarea no duplica un elemento de línea.
- NRPS está deshabilitado cuando el acceso a la lista de curso no sea necesario.
- Cada URL orientada a producción utiliza HTTPS público y un certificado de confianza.

## Solución de problemas

| Síntoma | Qué verificar |
| --- | --- |
| Falta **examina.io assessments** en **Find** | Confirma que la clave esté activada, que la App esté disponible para este curso y que la clave incluya la ubicación Assignment Selection con `LtiDeepLinkingRequest`. |
| El selector se abre pero Canvas rechaza el examen seleccionado | Confirma que Canvas pueda obtener la URL exacta de JWKS de examina.io específica del registro desde su red de servidores. La accesibilidad desde el navegador por sí sola no es suficiente. Verifica también el Client ID, el Deployment ID, el emisor y la precisión del reloj. |
| La tarea abre un marco en blanco o rechaza el inicio | Revisa la URL de inicio de OIDC, la URL de inicio, las URIs de redirección, el certificado HTTPS de confianza, la política de iframe y la configuración de cookies de terceros del navegador. Elimina cualquier nombre de host local, Docker o privado de la configuración de producción. |
| Se abre la evaluación incorrecta | Edita la tarea y vuelve a seleccionar la publicación. No copies una tarea entre entornos sin volver a seleccionar su contenido. |
| La calificación no aparece | Confirma que los alcances de AGS y **Grade return** estén habilitados, que la tarea tenga puntos y que la App siga disponible. Espera un momento para la entrega en cola. |
| La lista de curso no está disponible | Confirma que el alcance de NRPS y **Course roster** estén habilitados. El inicio y la devolución de calificaciones pueden continuar sin acceso a la lista. |
| Canvas informa un error de clave de firma | Canvas debe usar la URL de JWKS de examina.io específica del registro, y examina.io debe usar `https://<your-canvas-host>/api/lti/security/jwks`. Confirma que ninguno de los dos endpoints redirija a una página de inicio de sesión. |

Para conocer el comportamiento y la terminología actuales de la plataforma Canvas, consulta la documentación oficial de Instructure sobre [LTI registration](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.registration),
[Assignment Selection placement](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.assignment_selection_placement),
[Deep Linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item)
y [grading](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools).
