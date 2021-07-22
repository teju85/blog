---
layout: post
title: "Debloating Redmi 7A"
tags: android
---

Assuming you are inside the `adb shell`, running the below commands would remove
all the unnecessary apps from Redmi 7A. This does NOT require you to be root.
However, as expected, the .apk of these apps would still be available inside
`/data/app` folder.
```bash
pm uninstall --user 0 com.miui.compass                  # Mi Compass
pm uninstall --user 0 com.facebook.appmanager           # Facebook
pm uninstall --user 0 com.facebook.system
pm uninstall --user 0 com.facebook.services
pm uninstall --user 0 com.miui.yellowpage               # Mi Yellow Pages 
pm uninstall --user 0 com.mipay.wallet.in               # Mi Pay
pm uninstall --user 0 com.xiaomi.payment
pm uninstall --user 0 com.miui.weather2                 # Mi Weather
pm uninstall --user 0 com.miui.screenrecorder           # Screen Recorder
pm uninstall --user 0 com.miui.player                   # Music
pm uninstall --user 0 com.xiaomi.scanner                # Scanner
pm uninstall --user 0 com.xiaomi.midrop                 # ShareMe
pm uninstall --user 0 com.miui.analytics                # Analytics
pm uninstall --user 0 com.xiaomi.mipicks                # GetApps
pm uninstall --user 0 com.miui.android.fashiongallery   # Wallpaper Carousel (Got "Failure [-1000]"!!)
pm uninstall --user 0 com.miui.msa.global               # Mi Ads service
pm uninstall --user 0 com.miui.micloudsync              # Mi Cloud
pm uninstall --user 0 com.miui.cloudbackup
pm uninstall --user 0 com.miui.cloudservice
pm uninstall --user 0 com.miui.cloudservice.sysbase
pm uninstall --user 0 -k com.android.thememanager       # Themes
pm uninstall --user 0 com.xiaomi.glgm                   # Mi Games
pm uninstall --user 0 com.miui.backup                   # Mi Backup
pm uninstall --user 0 com.tencent.soter.soterserver     # Tencent app!?
pm uninstall --user 0 com.miui.bugreport                # Mi bug report
pm uninstall --user 0 com.miui.miservice                # Services & Feedback
pm uninstall --user 0 com.xiaomi.joyose                 # ??
pm uninstall --user 0 com.xiaomi.miplay_client          # MiPlayClient
pm uninstall --user 0 com.android.chrome                # Chrome browser (I use Firefox)
pm uninstall --user 0 com.netflix.partner.activation    # Netflix!?
pm uninstall --user 0 com.miui.miwallpaper              # Mi Wallpaper
pm uninstall --user 0 com.android.wallpaper.livepicker
pm uninstall --user 0 com.android.wallpaperbackup
pm uninstall --user 0 com.android.wallpapercropper
pm uninstall --user 0 com.xiaomi.xmsf                   # Xiaomi service framework
pm uninstall --user 0 com.xiaomi.xmsfkeeper
pm uninstall --user 0 com.miui.hybrid                   # Quick Apps
pm uninstall --user 0 com.miui.hybrid.accessory
pm uninstall --user 0 com.xiaomi.account                # Mi Account
pm uninstall --user 0 com.google.android.apps.wellbeing # Google Digital Wellbeing
pm uninstall --user 0 com.google.android.feedback       # Google feedback
pm uninstall --user 0 com.google.android.videos         # Google Play Movies & TV
pm uninstall --user 0 com.google.android.music          # Google Play Music
```
