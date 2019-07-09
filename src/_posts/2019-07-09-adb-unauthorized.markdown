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
0. Unplug your android device from the computer, if it is connected
1. Open your android device
2. Go to Settings -> Developer Options
3. Touch 'Revoke USB debugging authorizations'
4. Plug the device back into the computer
5. The device should now ask you for whether to trust this computer. Say yes.
