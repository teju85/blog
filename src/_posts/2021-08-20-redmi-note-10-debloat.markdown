---
layout: post
title: "Debloating Redmi Note 10"
tags: android
---

Assuming you are inside the `adb shell`, running the below commands would remove
all the unnecessary apps from Redmi Note 10. This does NOT require you to be root.
However, as expected, the .apk of these apps would still be available inside
`/data/app` folder.
```bash
pm uninstall --user 0 com.miui.screenrecorder                     # Screen recorder
pm uninstall --user 0 com.google.android.apps.subscriptions.red   # Google One
pm uninstall --user 0 com.xiaomi.miplay_client                    # MiPlayClient
pm uninstall --user 0 com.miui.qr
pm uninstall --user 0 com.xiaomi.scanner                          # Mi Scanner
pm uninstall --user 0 com.google.android.apps.googleassistant     # Google Assistant
pm uninstall --user 0 com.milink.service                          # UniPlay service
pm uninstall --user 0 com.xiaomi.account                          # Mi Account
pm uninstall --user 0 com.xiaomi.mi_connect_service
pm uninstall --user 0 com.android.protips                         # home screen tips!?
pm uninstall --user 0 com.miui.msa.global                         # Mi Ads service
pm uninstall --user 0 com.mipay.wallet.in                         # Mi Pay
pm uninstall --user 0 com.xiaomi.payment
pm uninstall --user 0 com.google.android.googlequicksearchbox     # Google Search Box
pm uninstall --user 0 -k com.android.thememanager                 # Themes
pm uninstall --user 0 -k com.android.thememanager.module
pm uninstall --user 0 com.xiaomi.glgm                             # Mi Games
pm uninstall --user 0 com.miui.backup                             # Mi Backup
pm uninstall --user 0 android.autoinstalls.config.Xiaomi.qssi
pm uninstall --user 0 com.netflix.partner.activation              # Netflix background app!?
pm uninstall --user 0 com.miui.guardprovider                      # Mi GuardProvider
pm uninstall --user 0 com.miui.micloudsync                        # Mi Cloud
pm uninstall --user 0 com.miui.cloudbackup
pm uninstall --user 0 com.miui.cloudservice
pm uninstall --user 0 com.miui.cloudservice.sysbase
pm uninstall --user 0 com.xiaomi.micloud.sdk                      # Mi Cloud SDK (first remove the rest of the Cloud Apps!)
pm uninstall --user 0 com.miui.hybrid                             # Quick Apps
pm uninstall --user 0 com.miui.hybrid.accessory
pm uninstall --user 0 com.miui.player                             # Music
pm uninstall --user 0 com.miui.bugreport                          # Mi bug report
pm uninstall --user 0 com.miui.miservice                          # Services & Feedback
pm uninstall --user 0 com.facebook.appmanager                     # Facebook
pm uninstall --user 0 com.facebook.system
pm uninstall --user 0 com.facebook.services
pm uninstall --user 0 com.miui.compass                            # Mi Compass
pm uninstall --user 0 com.miui.android.fashiongallery             # Wallpaper Carousel
pm uninstall --user 0 com.miui.global.packageinstaller
pm uninstall --user 0 com.android.chrome                          # Chrome browser. Personal Choice: I use Firefox
pm uninstall --user 0 com.xiaomi.xmsf                             # Xiaomi service framework
pm uninstall --user 0 com.xiaomi.xmsfkeeper
pm uninstall --user 0 com.xiaomi.mipicks                          # GetApps
pm uninstall --user 0 com.xiaomi.joyose
pm uninstall --user 0 com.xiaomi.midrop                           # ShareMe
pm uninstall --user 0 com.tencent.soter.soterserver               # Some random Tencent app!?
pm uninstall --user 0 com.miui.miwallpaper                        # Mi Wallpaper
pm uninstall --user 0 com.android.wallpaper.livepicker
pm uninstall --user 0 com.android.wallpaperbackup
pm uninstall --user 0 com.android.wallpapercropper
pm uninstall --user 0 com.miui.analytics                          # Analytics
pm uninstall --user 0 com.miui.yellowpage                         # Mi Yellow Pages
pm uninstall --user 0 com.miui.weather2                           # Mi Weather
pm uninstall --user 0 com.facemoji.lite.xiaomi                    # FaceMoji (Gives error: Failure [-1000])
pm uninstall --user 0 com.google.android.apps.wellbeing           # Google Digital Wellbeing
pm uninstall --user 0 com.google.android.feedback                 # Market Agent Feedback
pm uninstall --user 0 com.google.android.marvin.talkback
pm uninstall --user 0 com.android.soundrecorder                   # Mi Recorder

# Safer/Better to keep these
# com.miui.extraphoto             (used inside stock camera)
# com.miui.gallery                (removing this can cause soft brick!)
# com.miui.daemon                 (remove at your own risk!)
# com.miui.securitycore           (core security)
# com.miui.fm                     (FM Radio. Personal Choice: I use it)
# com.miui.fmservice
# com.miui.vsimcore               (needed for "Mi Roaming")
# com.miui.rom                    (supposedly a core component of MIUI?)
# com.xiaomi.location.fused       (Geolocation over networks)
# com.miui.freeform               (Freeform - helps run apps in windows)
# com.google.android.documentsui  (DocumentsUI)
# com.miui.face                   (MI BioMetric)
# com.miui.core

# Undecided whether to keep/remove
#? com.xiaomi.simactivate.service         (Sim Activation Service)
#? com.xiaomi.finddevice
#? com.mi.android.globalFileexplorer      (Mi File Manager?)
#? com.miui.notes                         (Mi Notes)
#? com.miui.calculator                    (Mi Calculator)
#? com.xiaomi.bluetooth                   (only com.android.bluetooth is enough?)
#? com.miui.cleanmaster                   (Cleaner app)
#? com.google.android.apps.nbu.paisa.user (Indian version of GPay!?)
#? com.xiaomi.calendar                    (only com.android.calendar is enough?)
#? com.miui.audioeffect                   (MusicFX)
#? com.xiaomi.powerchecker
#? com.miui.powerkeeper

# in case you figure out the (name and/or) purpose of these, let me know
#??? miui.systemui.plugin
#??? com.miui.securityadd
#??? com.miui.securitycenter
#??? com.lctautotest.current
#??? com.longcheertel.sarauth
#??? com.miui.phrase
#??? org.codeaurora.ims
#??? com.miui.system
#??? com.miui.maintenancemode
#??? com.miui.aod
#??? com.miui.misound
#??? com.fido.xiaomi.uafclient
#??? com.fido.asm
#??? com.miui.wmsvc
#??? com.xiaomi.misettings
#??? com.miui.audiomonitor
#??? com.miui.touchassistant
#??? com.mi.android.globalminusscreen
#??? com.longcheertel.AutoTest
#??? com.google.android.projection.gearhead
#??? com.caf.fmradio
#??? com.longcheertel.cit
#??? com.mi.globallayout
#??? com.xiaomi.discover
#??? com.miui.home
```
