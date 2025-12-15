---
title: Wyoming Installation
sidebar_position: 3
---

# Wyoming Installation and configuration

Wyoming is a crossplatform means of receiving audio and providing results to Home Assistant.  You can choose Wyoming as your microphone device on any of the supported platforms.

A project exists for using [Wyoming with Termux](https://github.com/T-vK/wyoming-satellite-termux) on Android.  This has a level of difficulty that is much higher than your average app install.  This page will list the basic steps but support should be aimed at the project issues rather than View Assist support.  Feel free to provide updates to this page to make it easier for others to get this installed.

## Installation

* Install Termux on your Android device.  You may need to get this from Fdroid
* Install Termux API on your Android device.  You may need to get this from Fdroid
* Open the project page on the Android device and [copy the installation command](https://github.com/T-vK/wyoming-satellite-termux?tab=readme-ov-file#how-to-install)
* Open Termux on the Android device and paste in the command
* Watch for interactive prompts and answer defaults for all but do install OpenWakeword when prompted.  You may see popups for device permissions.  Allow all of them.
* At the end of the install.  At the end Launch Wyoming Openwakeword and Wyoming Satellite now say yes.
* Try giving a command but note any errors. The first time will probably result in things not working.  If this happens, run the installation command again.
* On the second run you may be asked about installing OpenWakeword again.  Say yes.
* Once the second install is complete you will need to add a Wyoming device in Home Assistant by going to Devices & Services -> Add -> Wyoming.  Enter the IP address and keep the port as default
* You can try the device and see if it recognizes and responds
* Issue the command `cd ~; rm wyoming-satellite-android; ln -s .termux/boot/wyoming-satellite-android .; cp .termux/boot/wyoming-satellite-android wyoming-satellite-android.bak`
* Edit the configuration file using `nano wyoming-satellite-android` .  You will want to at least change the name so that it is unique
* Create a new file `nano ~/.bashrc` and add the line `bash ~/wyoming-satellite-android`
* Force close Termux and clear cache
* Reopen Termux and Wyoming should start with your changes
