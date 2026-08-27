---
title: "Sandbox para desarrolladores"
description: "Prueba la API de examina.io de forma segura con datos aislados, claves de API de prueba, intentos de examen gratuitos, cuotas, retención y reinicio de sandbox."
tags: [examina api sandbox, test api, test exam integration, developer environment]
translation_source: integrations/developer-sandbox.md
translation_source_sha256: c718f56012f845a3f038bc8acabc33a951bd510f885f20e027d776fe66f55f1e
---

# Sandbox para desarrolladores

El sandbox para desarrolladores de examina.io es un entorno de prueba aislado alojado en `https://sandbox.examina.io`. Utiliza la infraestructura de la aplicación de producción sin compartir los exámenes, candidatos, resultados, claves de API, webhooks o el estado de facturación de tu organización en vivo.

Úsalo para validar las integraciones de aprovisionamiento, asignación, sesión de inicio, resultados y webhooks antes de enviar tráfico en vivo.

## Abre tu sandbox

Cada organización en vivo puede usar un sandbox. Cualquier usuario verificado de la organización puede abrirlo:

1. Inicia sesión en el panel principal en vivo.
2. Abre **Configuración → Sandbox para desarrolladores**.
3. Selecciona **Abrir sandbox**.

La primera visita crea automáticamente el sandbox aislado. Luego, examina.io te inicia sesión en `sandbox.examina.io` con una transferencia de navegador única y de corta duración, por lo que normalmente no hay una segunda pantalla de inicio de sesión. La transferencia no contiene ninguna contraseña ni credencial de sesión reutilizable y no se puede volver a ejecutar después de usarse.

El banner persistente de **MODO DE PRUEBA** y el estilo visual de prueba indican que el panel actual está utilizando datos del sandbox. No hay un conmutador de entorno: el nombre de host es el límite del entorno.

## Crea una clave de API de prueba

Desde la **Configuración** del sandbox, crea una clave de prueba con alcance delimitado. Los tokens de prueba comienzan con `exm_test.` y se muestran solo una vez. Envíalos únicamente a la URL base de la API del sandbox:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_TEST_API_KEY" \
  --header "Accept: application/json" \
  "https://sandbox.examina.io/api/v1/exams"
```

El límite se aplica en ambas direcciones:

- Las claves `exm_test.` funcionan únicamente en `sandbox.examina.io` y solo para el entorno sandbox vinculado.
- El sandbox rechaza las claves `exm_live.` y la autenticación básica (Basic Authentication) heredada.
- La API en vivo rechaza las claves de prueba.

Los eventos de webhook firmados del sandbox incluyen `"livemode": false` y `"environment": "test"`, lo que permite a los receptores mantener los eventos de prueba fuera de los flujos de trabajo secundarios en vivo.

Usa las mismas rutas de v1, cuerpos de solicitud, alcances y comportamiento de idempotencia que se muestran en la [referencia de la API](../api/index.md).

## Límites del sandbox

El sandbox de infraestructura compartida es intencionalmente pequeño y gratuito:

| Recurso | Límite |
| --- | ---: |
| Candidatos | 1 |
| Exámenes activos | 3 |
| Grupos | 3 |
| Intentos de examen | 5 por período de 30 días |
| Sesiones de examen concurrentes | 1 |
| Retención de resultados completados | 30 días |
| Solicitudes de API | 120 por clave de prueba por minuto |
| Reinicios del sandbox | 3 por día |

Los intentos en el sandbox nunca reservan fondos, no consumen cuotas de planes de pago, no escriben en registros de uso ni generan cargos por características facturables. Volver a conectarse al mismo intento no consume otro cupo de la cuota.

Las funciones externas de pago, como la supervisión de exámenes en vivo y la verificación de identidad, no están disponibles en el sandbox. La entrega de correos electrónicos y la grabación están deshabilitadas.

## Reinicia los datos de prueba

Un Administrador puede usar **Reiniciar sandbox** desde la Configuración del sandbox hasta tres veces por día. El reinicio elimina los exámenes de prueba, candidatos, grupos, asignaciones, resultados, configuración de webhooks, registros de entrega y archivos subidos al sandbox.

El reinicio conserva deliberadamente:

- el entorno sandbox;
- las claves `exm_test.` delimitadas; y
- el uso actual de la cuota de intentos de 30 días.

Conservar la cuota evita que el reinicio se convierta en una forma de eludir el límite de uso gratuito. Revoca las claves por separado cuando ya no sean necesarias.

## Retención de datos e indexación

Los resultados completados del sandbox se eliminan automáticamente después de 30 días. Las páginas del sandbox envían `X-Robots-Tag: noindex, nofollow`; el contenido del entorno de prueba no está destinado a la indexación en buscadores. La documentación pública para desarrolladores permanece indexable en `docs.examina.io`.

## Flujo de trabajo de integración recomendado

1. Desarrolla con respecto a `https://sandbox.examina.io/api/v1` utilizando una clave `exm_test.`.
2. Pon a prueba las rutas de éxito, validación, idempotencia, reintento y firma de webhooks.
3. Confirma que tu integración controle las respuestas de cuota del sandbox sin bucles de reintento.
4. Crea una clave `exm_live.` independiente con los alcances mínimos requeridos.
5. Cambia tanto la URL base como el secreto mediante la configuración de despliegue específica del entorno; nunca transformes un token de prueba en un token en vivo.

Para obtener solicitudes listas para copiar y realizar una primera prueba completa, sigue la [guía de inicio rápido de la API del sandbox](sandbox-api-quickstart.md).

## Solución de problemas de acceso

Si la transferencia automática expira o ya se utilizó, vuelve a la página de configuración **Sandbox para desarrolladores** en vivo y vuelve a seleccionar **Abrir sandbox**. Una transferencia expira después de 90 segundos. El inicio de sesión directo en `sandbox.examina.io` sigue estando disponible como alternativa.

Si las llamadas a la API devuelven HTTP 429, espera al período especificado en `Retry-After` antes de volver a intentarlo. Usa un algoritmo de retroceso exponencial limitado y no inicies bucles de reintento en paralelo.
