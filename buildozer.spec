[app]

title = City Defender
package.name = citydefender
package.domain = org.test

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
requirements = python3,kivy

# قبول الرخصة تلقائي
android.accept_sdk_license = True

# ده التعديل المهم: archs بدل arch
android.archs = arm64-v8a

android.api = 31
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET,VIBRATE

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
