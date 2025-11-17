---
sidebar_position: 3
title: "Step Two: Microphone Devices"
---

# Installing Microphone Input Devices

In order to leverage your tablet or other device as a voice assistant satellite, you'll need to have an application installed that will be responsible for providing audio input to Home Assistant for processing.

Several options exist for getting microphone data from your Android device to Home Assistant.

**You need to pick ONE of the following:**

- [View Assist Companion App](./vaca.md) - Recommended. The View Assist Companion App (VACA) is an Android application and integration written by View Assist developer Mark Parker. This combination provides a simple to install means of providing both microphone input and display output but also provides tons of additional functionality. VACA creates an Home ASsistant Assist Satellite device providing even more HA native functions. Click the link for installation instructions. **BE SURE TO INSTALL thE View Assist Companion App INTEGRATION!!!** Skipping the installation of the VACA integration is by far the cause of most problems people have with using it with View Assist.
- [HassMic](./hass-mic.md) - HassMic is a standalone application and integration that works great with View Assist. While not technically a part of the VA project, the author has worked hand in hand with the View Assist team to ensure full compatibility and provides information used by View Assist
- [Wyoming Satellite on Android](./wyoming.md) - VA user pantherale0 provides a guide to get Wyoming satellite capabilities with on device wake word detection on Android. This is fantastic but does have a more complicated install. Definitely worth checking out if you are techinical enough to install
- [Stream Assist](./stream-assist.md) - This is the orignal method for getting microphone to Home Assistant. While it does still work, it is more involved to set up and response time is slower than using either of the alternatives above. We will, however, continue to support it but do encourage folks to try the alternatives.
