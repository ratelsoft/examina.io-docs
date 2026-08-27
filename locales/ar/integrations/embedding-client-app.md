---
title: تضمين تطبيق العميل examina.io
description: أضف اختبار examina.io إلى موقع الويب الخاص بك باستخدام عنصر واجهة مستخدم
  العميل، والمجالات المعتمدة، والتحجيم سريع الاستجابة، وتسجيل الدخول التلقائي الآمن
  الاختياري.
tags:
- القطعة العميل
- امتحان التضمين
- تكامل الامتحان
- com.iframe
- جافا سكريبت
translation_source: integrations/embedding-client-app.md
translation_source_sha256: 6f480dd668adcac7c3052eb0cb74773a0e6581bfcdc08141f994a2c9e426827a
---

# تضمين تطبيق العميل على موقع الويب الخاص بك {#embed-the-client-app-on-your-website}

تستبدل أداة العميل رابط الاختبار بإطار iframe حتى يتمكن الممتحنين من إجراء الاختبار
التقييم داخل موقع معتمد.

أنت بحاجة إلى:

- حساب examina.io وخطة تدعم التضمين؛
- الوصول إلى **الصفحة الرئيسية → الإعدادات**؛
- امتحان مستورد إلى Manager؛
- إذن لتحرير الموقع المضيف؛ و
- المعرفة الأساسية بـ HTML.

## 1. قم بإنشاء مفتاح API عام {#1-create-a-public-api-key}

افتح **الصفحة الرئيسية → الإعدادات → مفاتيح API وخطاف الويب** وأنشئ **مفتاح API العام**.

![المنطقة الرئيسية API في إعدادات المؤسسة](../assets/images/embedding-client-app/api_section_1.jpg)

يستخدم التضمين البسيط المفتاح العام فقط. لا تضع المفتاح السري API بالداخل
رمز المتصفح.

تتطلب إعادة إنشاء المفتاح العام تحديث كل تثبيت لعنصر واجهة المستخدم.

## 2. الموافقة على نطاق موقع الويب {#2-approve-the-website-domain}

في **النطاقات المعتمدة والنطاقات الفرعية لتضمين عناصر واجهة المستخدم**:

1. أدخل اسم المضيف بدون بروتوكول أو مسار.
2. حدد **إضافة نطاق**.

على سبيل المثال، أدخل `assessment.example.edu`، وليس
`https://assessment.example.edu/exams`.

![قائمة النطاقات المعتمدة لعنصر واجهة المستخدم ](../assets/images/embedding-client-app/domain_section.jpg)

للاختبار المحلي، أضف اسم المضيف الذي تستخدمه بالفعل، مثل `localhost` أو
`127.0.0.1`; لا تشمل المنفذ. قم بإزالة مضيفي التطوير بعد الاختبار.
تجنب السماح لكل مجال في الإنتاج.

## 3. قم بتحميل البرنامج النصي للقطعة {#3-load-the-widget-script}

أضف البرنامج النصي لعنصر واجهة المستخدم إلى الصفحة واستبدل `YOUR_PUBLIC_API_KEY`:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Take the assessment</title>
  <script
    src="https://www.examina.io/client/widget.js?apiKey=YOUR_PUBLIC_API_KEY">
  </script>
</head>
<body>
  <h1>Readiness assessment</h1>
</body>
</html>
```

إذا كان المفتاح مفقودًا أو غير صالح، فلن يتم تحميل البرنامج النصي لعنصر واجهة المستخدم بشكل صحيح.

## 4. أضف رابط الامتحان {#4-add-the-exam-link}

في Manager، حدد الاختبار واختر **فتح رابط الاختبار**. انسخ عنوان URL.

![ابحث عن رابط الامتحان في Manager](../assets/images/embedding-client-app/manager_exam_details.jpg)

أضف الرابط مع فئة `examina-io-client-widget`:

```html
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID">
  Open the exam
</a>
```

عندما يكون JavaScript متاحًا، يستبدل عنصر واجهة المستخدم المرساة بالجزء المضمن
العميل. يظل نص الرابط بمثابة بديل مفيد إذا تعذر تشغيل البرنامج النصي.
ضع نقطة ارتساء عنصر واجهة مستخدم واحدة فقط على الصفحة.

## التحكم في أبعاد القطعة {#control-the-widget-dimensions}

تستخدم الأداة هذه السمات الاختيارية:

- `data-examina-io-height`
- `data-examina-io-width`

إذا تم حذف إحدى السمات، فسيقوم عنصر واجهة المستخدم بإدارة هذا البعد بالنسبة إلى
نافذة المتصفح ويمكن تعديلها عند تغيير حجم النافذة.

الاستخدام:

- رقم موجب لبعد بكسل ثابت؛
- رقم سالب لاستخدام حجم النافذة مطروحًا منه عدد البكسل هذا؛ أو
- `auto` لترك هذا البعد لـ CSS أو إعدادات المتصفح الافتراضية.

يحجز هذا المثال 64 بكسل لرأس الصفحة ويتيح لـ CSS إدارة العرض:

```html
<header class="exam-header">Readiness assessment</header>
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID"
  data-examina-io-height="-64"
  data-examina-io-width="auto">
  Open the exam
</a>
```

اختبر على أصغر إطار عرض مدعوم. عند استخدام `auto`، قم بتطبيق الأمر الصريح
حجم CSS إلى التخطيط الناتج بحيث لا يكون حجم iframe الافتراضي للمتصفح
تستخدم عن طريق الخطأ.

## مثال استجابة كاملة {#complete-responsive-example}

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Readiness assessment</title>
  <script
    src="https://www.examina.io/client/widget.js?apiKey=YOUR_PUBLIC_API_KEY">
  </script>
  <style>
    html, body { margin: 0; }
    .exam-header { box-sizing: border-box; height: 64px; padding: 20px; }
  </style>
</head>
<body>
  <header class="exam-header">Readiness assessment</header>
  <a
    class="examina-io-client-widget"
    href="https://www.examina.io/client/YOUR_EXAM_ID"
    data-examina-io-height="-64"
    data-examina-io-width="auto">
    Open the exam
  </a>
</body>
</html>
```

## تسجيل الدخول التلقائي الاختياري {#optional-autologin}

إذا كان موقعك قد قام بالفعل بمصادقة الممتحن، فيمكن للواجهة الخلفية الخاصة بك القيام بذلك
اطلب رمزًا مميزًا لتسجيل الدخول للاختبار قصير الأمد وأضفه إلى رابط العميل. API
يجب أن يبقى المفتاح السري على الخادم الخاص بك.

التدفق الخلفي:

1. قم بالمصادقة على الشخص المذكور في طلبك.
2. قم بحل رمز أو معرف الممتحن examina.io على الخادم.
3. من الخادم الخاص بك، اتصل بإحدى نقاط نهاية الرمز المميز الموثقة باستخدام HTTPS
   المصادقة الأساسية:
   - `/login/exam/{examId}/code/{examineeCode}/token`
   - `/login/exam/{examId}/id/{examineeId}/token`
4. أنشئ عنوان URL للعميل باستخدام قيم الاستعلام المشفرة بعنوان URL.
5. قم بتقديم المفتاح العام وعنوان URL لتسجيل الدخول المحدود المدة إلى الصفحة المعتمدة.

مثال على شكل الرابط:

```html
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID?autologin=true&amp;examineeCode=URL_ENCODED_CODE&amp;token=URL_ENCODED_TOKEN"
  data-examina-io-height="-64"
  data-examina-io-width="auto">
  Open the exam
</a>
```

يجب أن يكون `autologin` هو `true`. قم بتوريد `examineeCode` أو `examineeId`؛
عندما يكون كلاهما موجودا، يستخدم العميل رمز الممتحن.

لا تقم أبدًا بإنشاء الرموز المميزة في متصفح JavaScript، وقم بكشف المفتاح السري لملف
الممتحن، أو قم بتسجيل عنوان URL الكامل لتسجيل الدخول التلقائي.

## قائمة مرجعية الإنتاج {#production-checklist}

- تمت الموافقة على اسم مضيف الإنتاج الدقيق.
- الصفحة وجميع الموارد المضمنة تستخدم HTTPS.
- المفتاح السري API غائب عن مصدر الصفحة وطلبات شبكة المتصفح.
- الرابط الاحتياطي مفهوم.
- القطعة واحدة موجودة على الصفحة.
- تم اختبار سلوك سطح المكتب والجوال ولوحة المفاتيح وتغيير الحجم.
- يمكن للممتحن الخيالي تسجيل الدخول أو تسجيل الدخول تلقائيًا وإكمال الاختبار.
- تمت إزالة مجالات التطوير المؤقتة.

لإعداد بيانات الاعتماد والتدوير، راجع [مفاتيح API و
خطافات الويب](api-keys-and-webhooks.md). بالنسبة لمخططات نقطة النهاية، استخدم الملف [API
مرجع](../api/index.md).
