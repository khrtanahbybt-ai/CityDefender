[app]

# اسم اللعبة
title = City Defender

# اسم الباكدج
package.name = citydefender
package.domain = org.test

# السورس كود
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf

# اصدار اللعبة
version = 0.1

# المكتبات المطلوبة
requirements = python3,kivy

# اهم سطر عشان يقبل الرخصة وينزل build-tools
android.accept_sdk_license = True

# اصدارات الاندرويد
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.sdk_path =

# نوع المعالج
android.arch = arm64-v8a

# صلاحيات اللعبة
android.permissions = INTERNET,VIBRATE

# ايقونة اللعبة - لو عندك صورة حط اسمها هنا
#icon.filename = %(source.dir)s/icon.png

# اتجاه الشاشة
orientation = portrait

# اللوجو وقت التحميل
presplash.filename = %(source.dir)s/presplash.png

# اصدار الـ buildozer
buildozer.version = 1.5.0

[buildozer]

# مسار الـ logs
log_level = 2

# مكان تخزين الـ SDK والـ NDK
android.sdk_path =
android.ndk_path =

# توقيع الـ APK
android.release_artifact = apk
