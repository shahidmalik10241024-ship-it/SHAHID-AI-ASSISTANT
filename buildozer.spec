[app]
title = SHAHID AI ASSISTANT
package.name = shahidaiassistant
package.domain = org.shahid
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android permissions for future speech integration.
# This starter app DOES NOT yet provide always-on/background listening.
android.permissions = INTERNET,RECORD_AUDIO
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
