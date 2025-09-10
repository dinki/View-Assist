---
title: Lenovo Smart Display
sidebar_position: 2
---

There are three Lenovo Smart Displays, all of which are ~similar to the Lenovo Thinksmart View.
- The Lenovo Smart Display 7" (CD-17302F);
- The Lenovo Smart Display 8" (SD-8501F); and
- The Lenovo Smart Display 10" (SD-X701B)

All of these devices run Android Things, the Android IOT platform, which is a stripped down version of Android 8.

At a high level, to get View Assist and View Assist Companion App working on these devices, you need to:
1. Unlock them and flash them with firmware that lets you run ADB commands;
1. Update them so they have a more modern webview;
1. Disable some of the built in software; and
1. Install VACA.

# Unlocking and Flashing

For the Lenovo Smart Display 7 follow these instructions[https://xdaforums.com/t/cd-17302f-lenovo-smart-display-7-ivy-avb-bootloader-unlock-firmware.4472041/].

For the Lenovo Smart Display 8 and 10 follow [these instructions](https://xdaforums.com/t/lenovo-smart-display-8-10-amber-blueberry-avb-bootloader-unlock-firmware.4472049/).

# Updating

After unlocking and flashing them, with them connected to your computer, run `adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME` on your compute to bring up settings on the device. (Note after unlocking and flashing them, you will not be able to go through the normal set up flow.)

Connect them to WiFi and then update them. The goal of this update to get a more current WebView installed (~87).

# Disabling Built Ins

For performance and usability purposes, you should follow [these instructions](https://xdaforums.com/t/lenovo-smart-display-8-10-amber-blueberry-avb-bootloader-unlock-firmware.4472049/page-10#post-89766621) to disable software that is not needed as you're running VACA on these devices.

# Installing VACA

Install [Mark Parker's](https://github.com/msp1974) [View Assist Companion App](https://github.com/msp1974/ViewAssist_Companion_App) using `adb install`.