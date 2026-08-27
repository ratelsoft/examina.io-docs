---
title: "Envía correos electrónicos a tus candidatos"
description: "Envía invitaciones y resultados de exámenes desde examina.io Manager usando marcadores de posición, incluyendo enlaces que inician sesión directamente."
tags: [exam invitation, examinee email, magic link, manager, placeholders]
translation_source: user-guides/manager/email-examinees.md
translation_source_sha256: 5fc7cb4dd93fe7848375d20f62bf4c1a125a37385e6efd89d174ef4a5460b211
---

# Envía correos electrónicos a tus candidatos

Manager puede enviar correos electrónicos a las personas asignadas a un examen: una invitación antes de la sesión o sus resultados después. Ecribes el mensaje una vez y Manager lo personaliza para cada destinatario antes de enviarlo.

Selecciona el examen y luego usa **Enviar correo a candidatos** desde el panel de candidatos asignados. Solo los candidatos que tengan una dirección de correo electrónico en su registro recibirán un mensaje.

## Marcadores de posición de personalización

Escribe `#[CODE]` en tu mensaje y cada candidato recibirá su propio código en su lugar. Los marcadores de posición funcionan tanto en la línea de asunto como en el cuerpo del mensaje.

### El candidato

| Marcador de posición | Resultado |
|---|---|
| `#[FNAME]` | Nombre |
| `#[MNAME]` | Segundo nombre, o nada |
| `#[LNAME]` | Apellido |
| `#[FLNAME]` | Nombre completo |
| `#[TITLE]` | *Sr.* o *Sra.*, según el género registrado |
| `#[GEN]` | Género como texto |
| `#[CODE]` | Código o ID del candidato |
| `#[PASS]` | Contraseña |
| `#[EMAIL]` | Dirección de correo electrónico |
| `#[PHONE]` | Número de teléfono, o nada |
| `#[DOB]` | Fecha de nacimiento |
| `#[PIC]` | La fotografía del candidato, como imagen |

### El examen

| Marcador de posición | Resultado |
|---|---|
| `#[EXAM]` | Título del examen |
| `#[ECODE]` | Código del examen |
| `#[LINK]` | El enlace del examen, como enlace con clic |
| `#[MAGICLINK]` | Un enlace de inicio de sesión para ese candidato específico (consulta más abajo) |
| `#[TIME]` | La hora de inicio asignada al candidato, o nada si no se definió una hora |
| `#[PAPERS]` | Las evaluaciones a las que está asignado este candidato |

### El resultado

| Marcador de posición | Resultado |
|---|---|
| `#[SCORE]` | Calificación obtenida |
| `#[MAX]` | Calificación máxima posible |
| `#[PERCENT]` | Calificación como porcentaje |
| `#[RESULT]` | Un resumen del resultado con formato |

!!! warning "Los marcadores de posición de resultados solo deben ir en un correo de resultados"
    Estos marcadores leen los datos de un intento completado. En una invitación, enviada antes de que alguien rinda el examen, no hay ninguna calificación que sustituir y no mostrarán nada, lo que dejará una oración con un espacio vacío. Mantén estos marcadores fuera de las invitaciones.

## Enlaces de inicio de sesión

`#[MAGICLINK]` inserta un enlace que inicia la sesión de ese candidato directamente en su examen. No tiene que escribir un código ni una contraseña; el enlace contiene su identidad.

Vale la pena usar esto cuando la distribución de contraseñas es la parte complicada de tu proceso: candidatos más jóvenes, grupos grandes o cualquier persona que pueda equivocarse al escribir un código la mañana del examen.

```text
Hola, #[FNAME]:

Tu examen, #[EXAM], comienza a las #[TIME].

Ábrelo aquí: #[MAGICLINK]

Si el enlace no funciona, inicia sesión en #[LINK] con
el código #[CODE] y la contraseña #[PASS].
```

### Lo que debes saber antes de usarlo

**Envía también el código y la contraseña.** El correo electrónico es la parte menos confiable del día del examen: filtros, demoras o un candidato que lee el correo en un celular en el que no rendirá el examen. Considera el enlace como la vía conveniente y las credenciales como la alternativa de respaldo, tal como lo hace el ejemplo anterior.

**El enlace es personal y es una credencial.** Cualquier persona que lo posea puede rendir ese examen como ese candidato. Diles a los candidatos que no lo reenvíen. No es más compartible que una contraseña, pero es más fácil de reenviar por accidente.

**Un candidato no puede rendir el examen dos veces al mismo tiempo.** Si se abre el enlace mientras ese candidato ya tiene el examen abierto en otro lugar, se rechaza el segundo intento. Un candidato cuyo navegador se haya cerrado inesperadamente puede volver a abrir el mismo enlace y continuar.

**El enlace deja de funcionar cuando el examen termina.** Expira tres días después de enviarse, o poco después de que finalice la sesión cuando el candidato fue asignado con una hora de inicio. También deja de funcionar una vez que haya enviado el examen, si ocultas el examen o si eliminas su asignación.

**Es seguro volver a enviar.** Un correo electrónico de recordatorio vuelve a usar el enlace que ya está en la bandeja de entrada del candidato en lugar de reemplazarlo, por lo que el primer correo continúa funcionando.

### Cuando un enlace no funciona

El candidato llega a la página de inicio de sesión de ese examen con un mensaje que explica el motivo, y puede iniciar sesión con su código y contraseña en su lugar. Un enlace expirado lo indica claramente, a diferencia de un enlace que nunca fue válido para ese examen, de modo que no se le diga al candidato que sus credenciales son incorrectas cuando simplemente su enlace ha caducado.

La única excepción es un examen que ha sido eliminado. Ya no queda ningún examen para mostrar una página de inicio de sesión, por lo que el enlace dirige a una página de no encontrado.

## Antes de enviar

1. Envíate una prueba primero, usando un candidato de prueba asignado al examen.
2. Verifica que se hayan resuelto todos los marcadores de posición; uno mal escrito se enviará como texto literal.
3. Confirma que los destinatarios correspondan a la lista esperada en la lista de asignados del examen.
4. Compara la hora de inicio y la zona horaria del mensaje con la asignación.

## Próximo paso

Continúa con [Entregar, monitorear e informar](deliver-monitor-report.md).
