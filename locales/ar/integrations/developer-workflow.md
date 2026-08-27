---
title: سير عمل تكامل المطور
description: توفير الممتحنين، وإنشاء مهام الاختبار، وإصدار عناوين URL للاستخدام الفردي،
  واسترداد النتائج، ومزامنة أحداث الإكمال مع examina.io.
tags:
- واجهة برمجة التطبيقات للتقييم
- تكامل الامتحان
- lms API
- واجهة برمجة تطبيقات النتائج
translation_source: integrations/developer-workflow.md
translation_source_sha256: 95077cae1f14eaa9e4e46b5ab7917c976de504830eee6acddd0104191b7acb9c
---

# سير عمل تكامل المطور {#developer-integration-workflow}

يدعم الإصدار v1 API الرحلة الكاملة من خادم إلى خادم من المرشح
التزويد من خلال مزامنة النتائج.

لاختبار التكامل في مرحلة ما قبل الإنتاج، استخدم [developer sandbox](developer-sandbox.md)
مع عنوان URL الأساسي للاختبار فقط وبيانات اعتماد `exm_test.`. مسارات نقطة النهاية و
عقود الطلب هي نفس الإصدار المباشر API.

## 1. توفير الممتحنين {#1-provision-an-examinee}

قم بإنشاء ممتحن واحد باستخدام `POST /examinees`، أو قم بمزامنة ما يصل إلى 500 سجل
مع `POST /examinees/bulk-upsert`. يتطابق الإدخال المجمع مع السجلات حسب المؤسسة
ورمز الممتحنين. يتم تطبيع الرموز إلى الأحرف الكبيرة.

للحصول على رقم قياسي جديد، قم بتوفير `firstName`، و`lastName`، و`passcode`. يجوز لك أن تغفل
`code` أن يقوم examina.io بإنشاء واحد. تواريخ الميلاد تستخدم `YYYY-MM-DD`.

```json
{
  "code": "APPLICANT-1042",
  "passcode": "temporary-secret",
  "firstName": "Ada",
  "middleName": "N.",
  "lastName": "Okafor",
  "dateOfBirth": "2001-04-19",
  "gender": 0,
  "email": "ada@example.org"
}
```

يتم كتابة رموز المرور فقط في عقد الاستجابة الجديد.

## 2. قم بإنشاء مهمة {#2-create-an-assignment}

يربط `POST /assignments` ممتحنًا واحدًا باختبار واحد. تحديد الورق المحدد
العناوين أو حذف `papers` لتعيين كل ورقة. العناوين الورقية حساسة لحالة الأحرف.

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "papers": ["Quantitative Reasoning", "English"],
  "startsAt": "2026-09-01T09:00:00-04:00[America/Toronto]",
  "exemptFromProctoring": false
}
```

لا يمكن تحديث المهمة أو حذفها إلا عندما تكون حالتها كذلك
`DISCONNECTED`. لا يمكن تغيير هوية الامتحان والممتحن.

## 3. قم بإصدار عنوان URL للإطلاق {#3-issue-a-launch-url}

أنشئ عنوان URL قصير العمر باستخدام `POST /exam-sessions`:

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "expiresInSeconds": 3600
}
```

يجب أن يكون الممتحن قد تم تعيينه بالفعل للامتحان. `launchUrl` الذي تم إرجاعه هو
للاستخدام مرة واحدة وتنتهي صلاحيته بعد 60 ثانية إلى 24 ساعة. فلا ترسلها إلا للمراد
الممتحن عبر قناة موثوقة.

## 4. استلام الإكمال {#4-receive-completion}

اشترك في نقطة نهاية خطاف الويب في `result.completed`. التحقق من توقيعه من قبل
معالجتها. يتضمن الحدث معرف النتيجة/المهمة المطلوب استرجاعه.

## 5. استرجاع النتيجة الرسمية {#5-retrieve-the-authoritative-result}

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/results?examId=EXAM_ID&page=1&pageSize=100"
```

تتضمن النتائج النتيجة الإجمالية، والحد الأقصى للدرجات، والنسبة المئوية، والطابع الزمني للإكمال،
وأعداد وعشرات لكل ورقة. يتم إرجاع المحاولات المكتملة فقط.

## أعد المحاولة بأمان {#retry-safely}

استخدم `Idempotency-Key` مميزًا لكل عملية إنشاء أو تحديث منطقية.
بعد انتهاء مهلة الشبكة، قم بإعادة إرسال نفس النص والمفتاح. تعامل مع HTTP 409 كحالة
أو تعارض العجز، HTTP 422 كمدخل غير صالح أو حد المورد، HTTP 429
كحد لمعدل الطلب، وHTTP 5xx مع التراجع الأسي المحدود.
