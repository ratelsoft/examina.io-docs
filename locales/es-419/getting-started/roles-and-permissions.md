---
title: "Roles y permisos de usuario en examina.io"
description: "Elige el rol adecuado (Root, Administrator, Regular o Invigilator) y usa Circles para limitar el acceso a exámenes y candidatos."
tags: [access control, account roles, circles, exam permissions, users]
translation_source: getting-started/roles-and-permissions.md
translation_source_sha256: f3a07ab346be91a3e2440c78660d0266283b6866d6780c44fe9103e0e0ed8676
---

# Roles y permisos de usuario

Los miembros del personal inician sesión como **Users**. Cada User tiene un rol de cuenta que controla qué áreas de la aplicación están disponibles. Los **Circles** reducen el acceso a exámenes y candidatos específicos.

Los candidatos no necesitan cuentas de User de personal; ingresan a través de un enlace al examen con sus credenciales de candidato.

## Roles de cuenta

| Rol | Uso recomendado | Acceso típico |
| --- | --- | --- |
| **Root** | El propietario principal de la organización | Administración de la organización, Users, Circles, Settings, facturación y los espacios de trabajo de Designer, Manager y Proctor elegibles |
| **Administrator** | Administradores de confianza de la plataforma | Users, Circles, Settings y los espacios de trabajo de Designer, Manager y Proctor elegibles; sin acceso a la facturación de la organización |
| **Regular** | Autores de preguntas, coordinadores de exámenes y otro personal operativo | Designer y Manager para recursos permitidos a través de Circles; pueden ver Circles relevantes y usar los espacios de trabajo de Proctor elegibles |
| **Invigilator** | Personal que solo realiza la supervisión de exámenes activos | Supervisión de exámenes asignados y habilitados |

Como las cuentas Root y Administrator pueden gestionar a otros miembros del personal y la configuración de la organización, asígnalas con moderación.

## Cómo afectan los Circles al acceso

Un Circle contiene tres tipos de miembros:

- **Users** que reciben acceso;
- **Exámenes** con los que pueden trabajar; y
- **Candidatos** a los que pueden ver o gestionar.

Por ejemplo, un Circle `BIO-201` podría contener al coordinador del curso y a los supervisores, el examen parcial y los estudiantes inscritos. El personal fuera de ese Circle no obtendría acceso solo por tener una cuenta Regular.

![Un Circle que muestra los conteos de candidatos, usuarios y exámenes](../assets/images/administration/circles-permissions.png)

## Modelo de roles recomendado

- Mantén una o dos cuentas Root cuidadosamente protegidas.
- Usa Administrator para las personas que mantienen Users, Settings de la organización o la estructura de Circles.
- Usa Regular para el trabajo diario de creación de preguntas y gestión de exámenes.
- Usa Invigilator cuando una persona solo necesite el espacio de trabajo de Proctor.
- Crea Circles en torno a límites de responsabilidad estables, como un curso, departamento, cliente o programa de exámenes.
- Revisa y retira el acceso cuando un miembro del personal cambie de responsabilidad.

## Lista de verificación de permisos

Antes de un examen:

1. Confirma que cada miembro del personal tenga el rol más bajo que permita realizar su trabajo.
2. Confirma que el examen y sus candidatos estén en el Circle previsto.
3. Confirma que cada User operativo esté en ese Circle.
4. Si la supervisión de exámenes está habilitada, confirma que los supervisores asignados puedan ver el examen.
5. Realiza una prueba con una cuenta que no sea de administrador para verificar el límite previsto.

Para obtener instrucciones de configuración, consulta [Users y roles de cuenta](../user-guides/administration/users-and-roles.md) y [Circles y permisos](../user-guides/administration/circles-and-permissions.md).
