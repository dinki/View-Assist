---
title: Sonoff NSPanel Pro 120
sidebar_position: 4
---

The [Sonoff NSPanel Pro 120](https://sonoff.tech/en-us/products/sonoff-nspanel-pro-smart-home-control-panel-120-type) is smart home controller you wire into mains in your house. 

It runs Android under-the-hood and works well with View Assist Companion App.

# Prepare NSPanel Pro 120

[seaky](https://github.com/seaky) has created an [application](https://github.com/seaky/nspanel_pro_tools_apk) to help control the panel and has instructions on how to root the device, update the webview, and install their app. 

# Install View Assist Companion App

Install [Mark Parker's](https://github.com/msp1974) [View Assist Companion App](https://github.com/msp1974/ViewAssist_Companion_App) using adb.

# Configure the Panel in Home Assistant

1. Adopt the VACA device in Home Assistant
1. Set the mic gain as appropriate for your environment. The author has devices set to 5.
1. Set the wake word threshold as appropriate. The author has devices set to 4.
1. Add the NSPanel as a View Assist device with a display.

Note that the mic gain and wake word settings are highly dependent on your environment given that the acoustics of this device will depend on the proximity of its mounting to door frames, other objects on the wall, etc.

Also, given the screen's size you may want to build a custom dashboard/view for this device and set the Panel's dashboard to point to that custom dashboard.

Finally, it is recommended to use the KITT style assistant notification for purposes of performance.