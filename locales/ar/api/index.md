---
title: مرجع API
description: مرجع REST API لدمج الأنظمة الخارجية مع examina.io.
hide:
- navigation
- toc
translation_source: api/index.md
translation_source_sha256: fa5b9458d5dda85f1776c6ff0ae12e0be9377b40effda1b3c259ebc42c9ecae1
---

# مرجع API {#api-reference}

يستبدل إصدار الإنتاج هذه الصفحة بمرجع API التفاعلي
تم إنشاؤها من [`reference/examina.io.v1.yaml`](https://github.com/ratelsoft/examina.io-docs/blob/main/reference/examina.io.v1.yaml).

تتم مصادقة عمليات التكامل الجديدة باستخدام مفتاح Bearer API المسمى والمحدد النطاق. تراث الأساسية
تظل المصادقة مدعومة أثناء الترحيل. تغيير نقاط نهاية المطور
تتطلب `Idempotency-Key`؛ راجع [سير عمل المطور ](../integrations/developer-workflow.md)
و[دليل الأمان ](../integrations/api-keys-and-webhooks.md).

استخدم `https://sandbox.examina.io/api/v1` مع مفتاح `exm_test.` للعزل،
اختبار التكامل غير القابل للفوترة. راجع [دليل وضع الحماية للمطورين ](../integrations/developer-sandbox.md)
للحصص النسبية والاحتفاظ وإعادة ضبط السلوك وقواعد عزل البيئة.
