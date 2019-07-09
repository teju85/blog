---
layout: post
title: "Resolving ADB unauthorized issue"
tags: android
---

### Issue
```bash
cd $ANDROID_SDK_HOME/platform-tools
adb devices
List of devices attached
fffffffffffffff        unauthorized
```
One would see the 'unauthorized' keyword in the place of the device name.
`adb shell` would also fail stating something about 'keys not set'.

### Solution
1. Unplug your android device from the computer, if it is connected
2. Inside your computer:
   - Go to `$ANDROID_SDK_HOME/platform-tools`
   - Run `adb keygen .android/adb_key`
3. Open your android device
4. Go to Settings -> Developer Options
5. Touch 'Revoke USB debugging authorizations'
6. Plug the device back into the computer
7. The device should now ask you for whether to trust this computer. Say yes.
