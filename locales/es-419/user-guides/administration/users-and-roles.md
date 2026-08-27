---
title: "Administra los usuarios y roles de la cuenta"
description: "Agrega usuarios del personal, elige roles de cuenta de examina.io, restablece accesos y aplica permisos con el privilegio mínimo."
tags: [account roles, administrators, invigilators, user management]
translation_source: user-guides/administration/users-and-roles.md
translation_source_sha256: 0de577eb6227a78de5c3212ee769ac9f5df03d7870c962fa0fd9a33b2883d719
---

# Administra los usuarios y roles de la cuenta

Los usuarios son cuentas del personal para crear, administrar o supervisar exámenes.
No son registros de candidatos.

Las cuentas Root y Administrator pueden abrir **Inicio → Usuarios**. La tabla de Usuarios
muestra el nombre, la dirección de correo electrónico y el tipo de cuenta de cada miembro visible del personal.

![La tabla de Usuarios con una cuenta de coordinador de exámenes de tipo Regular](../../assets/images/administration/users-and-roles.png)

## Elige un rol de cuenta

| Rol | Asignar a |
| --- | --- |
| **Root** | Un propietario principal de la organización que necesita facturación y administración completa de la organización |
| **Administrator** | Un administrador de confianza que gestiona usuarios, Circles y ajustes |
| **Regular** | Un autor de preguntas, coordinador de exámenes u otro miembro del personal que necesite Designer o Manager |
| **Invigilator** | Una persona que solo realiza la supervisión de exámenes en vivo elegibles |

Utiliza el rol más bajo que permita realizar el trabajo de la persona. Consulta [Roles de usuario y permisos](../../getting-started/roles-and-permissions.md) para conocer el modelo de acceso detallado.

## Agrega un usuario

1. Abre **Inicio → Usuarios**.
2. Selecciona **Agregar nuevo usuario**.
3. Ingresa el nombre de la persona y su dirección de correo electrónico laboral.
4. Elige el tipo de cuenta.
5. Envía el formulario.
6. Confirma que la persona complete el proceso requerido de verificación de cuenta o configuración de contraseña.
7. Agrega el usuario a los Circles correspondientes.

Utiliza una cuenta laboral individual para cada persona. Las credenciales compartidas de administrador o invigilator debilitan la responsabilidad y dificultan el proceso de baja.

## Restablece o elimina accesos

Los botones de acción en la tabla de Usuarios permiten que un administrador restablezca la contraseña de un usuario o elimine al usuario.

Antes de restablecer una contraseña, verifica la identidad del solicitante a través de un canal aprobado. Antes de eliminar a un usuario:

1. confirma la cuenta exacta;
2. revisa cualquier transferencia operacional de funciones;
3. elimina o reasigna las responsabilidades en los Circles;
4. conserva la información de auditoría requerida; y
5. notifica al propietario de la cuenta según las políticas.

Eliminar a un usuario del personal es diferente de eliminar a un candidato.

## Revisa los accesos con regularidad

Al menos antes de cada evaluación de alto impacto:

- elimina las cuentas de las personas que ya no necesiten acceso;
- reduce las cuentas de Administrator que ya no administren la plataforma;
- confirma que los Invigilators estén vinculados solo a los exámenes necesarios a través de Circles;
- verifica que los usuarios con rol Regular no puedan ver exámenes o candidatos no relacionados; y
- protege las cuentas Root con credenciales sólidas y únicas.

## Soluciona problemas de falta de acceso

Si un miembro del personal puede iniciar sesión pero no puede ver un examen o candidato:

1. confirma que el rol de la cuenta admita la aplicación requerida;
2. confirma que el usuario pertenezca al Circle correspondiente;
3. confirma que el examen y los candidatos se encuentren en ese mismo Circle; y
4. cierra sesión y vuelve a iniciar sesión después de realizar cambios de permisos cuando sea necesario.

Continúa con [Circles y permisos](circles-and-permissions.md).
