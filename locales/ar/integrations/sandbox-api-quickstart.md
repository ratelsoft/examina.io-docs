---
title: ساندبوكس API التشغيل السريع
description: قم بإجراء اختبار examina.io API الآمن والشامل باستخدام مفتاح وضع الحماية
  وممتحن واحد ومهمة وعنوان URL لبدء الاختبار للاستخدام الواحد.
tags:
- البدء السريع لفحص API
- البرنامج التعليمي لتقييم API
- واجهة برمجة تطبيقات رمل
- تكامل الامتحان
translation_source: integrations/sandbox-api-quickstart.md
translation_source_sha256: 8091d2d137179887e5a9857221371de160271055c4e2b83b7249be9abfb8416b
---

# التشغيل السريع لـ Sandbox API {#sandbox-api-quickstart}

تعمل هذه البداية السريعة على التحقق من المصادقة، وتوفير الممتحنين، والتعيين،
وإنشاء جلسة الامتحان دون لمس البيانات المباشرة أو الفواتير.

## قبل أن تبدأ {#before-you-begin}

افتح [صندوق الرمل للمطورين ](developer-sandbox.md)، وقم بتحميل أو إنشاء اختبار اختباري
في لوحة المعلومات الخاصة به، وقم بإنشاء مفتاح اختبار API باستخدام هذه النطاقات:

- `examinees:write`
- `assignments:write`
- `sessions:write`
- `exams:read`

قم بتخزين المفتاح ومعرف اختبار الاختبار في الصدفة الخاصة بك. لا تلتزم بأي من القيمتين:

```bash
export EXAMINA_BASE_URL="https://sandbox.examina.io/api/v1"
export EXAMINA_API_KEY="exm_test.REPLACE_WITH_YOUR_KEY"
export EXAMINA_EXAM_ID="REPLACE_WITH_YOUR_TEST_EXAM_ID"
```

## 1. تأكيد المصادقة {#1-confirm-authentication}

```bash
curl --fail-with-body \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "$EXAMINA_BASE_URL/exams"
```

يؤدي الطلب الناجح إلى إرجاع HTTP 200. ويتم رفض مفتاح الاختبار على المضيف المباشر،
ويتم رفض المفتاح المباشر على مضيف وضع الحماية.

## 2. إنشاء ممتحن الاختبار {#2-create-the-test-examinee}

يسمح صندوق الرمل بممتحن واحد. استخدم مفتاح العجز الذي يمثل هذا
طلب إنشاء منطقي:

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-examinee-v1" \
  --data '{
    "code": "SANDBOX-001",
    "passcode": "replace-with-a-temporary-secret",
    "firstName": "Sandbox",
    "lastName": "Candidate",
    "email": "developer@example.org"
  }' \
  "$EXAMINA_BASE_URL/examinees"
```

انسخ المستوى الأعلى `id` من استجابة HTTP 201:

```bash
export EXAMINA_EXAMINEE_ID="REPLACE_WITH_RETURNED_ID"
```

إعادة إرسال الطلب المتطابق باستخدام نفس مفتاح العجز يؤدي إلى إرجاع نفس الطلب
الموارد. إعادة استخدامه مع بيانات مختلفة يُرجع HTTP 409.

## 3. تعيين الممتحن {#3-assign-the-examinee}

حذف `papers` لتخصيص كل ورقة في الامتحان. إذا قمت بإدراجه، والعناوين الورقية
حساسة لحالة الأحرف.

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-assignment-v1" \
  --data "{
    \"examId\": \"$EXAMINA_EXAM_ID\",
    \"examineeId\": \"$EXAMINA_EXAMINEE_ID\",
    \"startsAt\": null,
    \"exemptFromProctoring\": true
  }" \
  "$EXAMINA_BASE_URL/assignments"
```

تحتوي استجابة HTTP 201 على معرف المهمة ودورة حياتها الحالية
الحالة.

## 4. قم بإنشاء عنوان URL للإطلاق للاستخدام مرة واحدة {#4-create-a-single-use-launch-url}

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-session-v1" \
  --data "{
    \"examId\": \"$EXAMINA_EXAM_ID\",
    \"examineeId\": \"$EXAMINA_EXAMINEE_ID\",
    \"expiresInSeconds\": 3600
  }" \
  "$EXAMINA_BASE_URL/exam-sessions"
```

افتح `launchUrl` الذي تم إرجاعه فقط عندما يكون جهاز الاختبار المقصود جاهزًا. إنه كذلك
للاستخدام الفردي وتنتهي صلاحيته في وقت `expiresAt` الذي تم إرجاعه.

## 5. التعامل مع فشل الاختبار {#5-test-failure-handling}

قبل الانتقال إلى بيانات الاعتماد المباشرة، تأكد من أن التكامل الخاص بك يتعامل مع:

- HTTP 401 لمفتاح البيئة المفقود أو المُبطل أو الخاطئ؛
- HTTP 403 لمفتاح يفتقد النطاق المطلوب؛
- HTTP 409 للعجز أو تعارض حالة المورد؛
- HTTP 422 للإدخال غير الصالح أو حصة الحماية؛
- HTTP 429 لحدود معدل الطلب؛ و
- استجابات HTTP 5xx عابرة مع تراجع أسي محدود.

يسمح وضع الحماية بـ 120 طلب API لكل مفتاح اختبار في الدقيقة. لا يتم شحنه أبدًا
يحاول أو ينشئ حالة الفوترة. عند اكتمال الاختبار، مسؤول
يمكن إعادة تعيين بيانات وضع الحماية من الإعدادات.

راجع [سير عمل تكامل المطورين ](developer-workflow.md) للحصول على النتائج و
تسليم خطاف الويب الموقع، و[API مرجع](../api/index.md) لكل
عقد الطلب والاستجابة.
