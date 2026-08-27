---
title: مفاتيح API ذات النطاق وخطافات الويب الموقعة
description: عمليات تكامل examina.io آمنة مع مفاتيح API المحددة، والطلبات غير الفعالة،
  وخطافات الويب للنتائج الموقعة، وسجل التسليم، والتدوير الآمن للمفاتيح.
tags:
- مصادقة واجهة برمجة التطبيقات
- مفاتيح واجهة برمجة التطبيقات ذات النطاق
- خطافات الويب الموقعة
- إعادة تشغيل خطاف الويب
translation_source: integrations/api-keys-and-webhooks.md
translation_source_sha256: 880a25fd36e3e26421e05743011286753915471d7ffe9b5722b21c91e7fe7001
---

# مفاتيح API ذات النطاق وخطافات الويب الموقعة {#scoped-api-keys-and-signed-webhooks}

يجب أن تستخدم عمليات التكامل الجديدة مفاتيح API المسماة والمحددة النطاق. يمكن إبطال كل مفتاح
دون مقاطعة عمليات التكامل الأخرى ويتلقى فقط الأذونات
الاحتياجات. تظل المفاتيح السرية للمؤسسة القديمة API متوافقة أثناء الترحيل.

## قم بإنشاء مفتاح API محدد النطاق {#create-a-scoped-api-key}

يقوم المسؤول بإنشاء المفاتيح من إعدادات المطور الخاصة بالمؤسسة. ال
يتم عرض الرمز المميز مرة واحدة فقط. تبدأ الرموز الحية بـ `exm_live.`؛
[تبدأ الرموز المميزة لـ sandbox](developer-sandbox.md) بـ `exm_test.`. متجر
كل رمز مميز في مدير سري من جانب الخادم.

| النطاق | يسمح |
| --- | --- |
| `examinees:read` | قراءة سجلات الممتحنين من خلال نقاط النهاية الموجودة |
| `examinees:write` | إنشاء وتحديث وتجميع الممتحنين |
| `exams:read` | إقرأ تعريفات الإمتحان |
| `exams:write` | تحميل الاختبارات وتكوينها ووضع علامة عليها وحذفها |
| `groups:read` | قراءة المجموعات وعضويتها |
| `groups:write` | إنشاء مجموعات وتغيير العضوية |
| `assignments:read` | قراءة واجبات الامتحان |
| `assignments:write` | إنشاء وتغيير وحذف المهام غير المبدئية |
| `results:read` | قراءة النتائج المكتملة والملخصات الورقية |
| `sessions:write` | إنشاء عناوين URL لإطلاق الاختبار ذات الاستخدام الواحد |
| `webhooks:read` | قائمة نقاط النهاية وتاريخ التسليم |
| `webhooks:write` | قم بإنشاء نقاط النهاية، وتعطيل نقاط النهاية، وأعد محاولة التسليم |

المصادقة باستخدام مخطط Bearer:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/results?page=1&pageSize=25"
```

لا تضع مفاتيح API في رمز المتصفح، وتطبيقات الهاتف المحمول، ولقطات الشاشة،
التحكم بالمصادر، أو سجلات الدعم.

مفاتيح API مرتبطة بالبيئة. يعمل مفتاح `exm_live.` فقط على API المباشر.
يعمل مفتاح `exm_test.` فقط على `https://sandbox.examina.io/api/v1`. تراث
يتم قبول المصادقة الأساسية فقط من خلال API المباشر.

## جعل الطفرات عاجزة {#make-mutations-idempotent}

يتطلب إنشاء نقاط النهاية وتحديثها رأس `Idempotency-Key`. توليد أ
قيمة فريدة للعملية المنطقية وإعادة استخدامها فقط عند إعادة محاولة ذلك
نفس الطلب:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: candidate-import-2026-08-23-0001" \
  --data '{"code":"CANDIDATE-42","passcode":"temporary-secret","firstName":"Ada","lastName":"Okafor"}' \
  "https://www.examina.io/api/v1/examinees"
```

يتم الاحتفاظ بالمفتاح لمدة 24 ساعة على الأقل. تكرار ذلك بجسد مماثل
إرجاع المورد الأصلي. إعادة استخدامه مع بيانات مختلفة يُرجع HTTP 409.

## قم بتكوين خطاف ويب موقع {#configure-a-signed-webhook}

قم بإنشاء نقطة نهاية مشتركة في `result.completed`:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: webhook-results-v1" \
  --data '{"url":"https://integrator.example/webhooks/examina","events":["result.completed"]}' \
  "https://www.examina.io/api/v1/webhook-endpoints"
```

تتضمن الاستجابة `signingSecret` بدءًا من `whsec_`. هو مبين
مرة واحدة فقط. يجب أن تستخدم عناوين URL الخاصة بخطاف الويب HTTPS العام ويجب ألا تتحول إلى عنوان خاص أو خاص.
الاسترجاع أو الارتباط المحلي أو عنوان البث المتعدد.

يحتوي كل تسليم على حدث JSON. ويتضمن الطلب أيضًا:

يتضمن مظروف الحدث `livemode` و`environment`. تسليمات رمل
استخدم `"livemode": false` و`"environment": "test"`؛ استخدام التسليم المباشر
`true` و `"live"`. رفض بيئة غير متوقعة قبل معالجة البيانات.

| رأس | معنى |
| --- | --- |
| `X-Examina-Event-Id` | معرف الحدث الثابت لإلغاء البيانات المكررة |
| `X-Examina-Timestamp` | الطابع الزمني لنظام Unix المستخدم في التوقيع |
| `X-Examina-Signature` | `v1=` متبوعًا بالتوقيع الست عشري HMAC-SHA256 |

قم بتسلسل الطابع الزمني والفترة ونص الطلب الأولي الدقيق. احسب
HMAC-SHA256 مع سر التوقيع ومقارنته بتوقيع `v1` باستخدام
مقارنة الزمن الثابت:

```text
signed_content = timestamp + "." + raw_request_body
expected = hex(HMAC_SHA256(signing_secret, signed_content))
```

قم بإرجاع استجابة 2xx بسرعة ووضع قائمة الانتظار للمعالجة لفترة أطول. استخدم معرف الحدث ل
قم بإلغاء المعالجة المكررة، ثم قم باسترداد النتيجة الموثوقة من
`GET /results/{assignmentId}`.

## فحص وإعادة محاولة عمليات التسليم {#inspect-and-retry-deliveries}

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries?page=1&pageSize=25"

curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries/DELIVERY_ID/retry"
```

يظل رد الاتصال السابق للنموذج على مستوى المؤسسة متاحًا للموجود
التكامل ولكن تم إهماله. يجب أن تستخدم عمليات التكامل الجديدة نقطة النهاية الموقعة
الموارد لأنها توفر معرفات الأحداث والتوقيعات وحالة التسليم وإعادة التشغيل.

## تدوير أو إلغاء بيانات الاعتماد {#rotate-or-revoke-credentials}

قم بإنشاء مفتاح بديل، ونشره لكل مستهلك، والتحقق من المكالمات الناجحة،
ثم قم بإلغاء المفتاح السابق. نظرًا لأن المفاتيح مستقلة، فإن التدوير يفعل ذلك
لا تتطلب قطعًا متزامنًا. قم بإلغاء المفتاح على الفور إذا كان من الممكن أن يكون كذلك
تم كشفها.
