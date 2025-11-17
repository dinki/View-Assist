---
sidebar_position: 4
title: "Step Three: Display Devices"
---

Setting up the display for View Assist consists of setting up a browser and also adding the necessary Lovelace prerequisites.

**Skipping the Lovelace prerequisites is the cause of most of the issues with View Assist so do not skip this step! See instructions in the second section below**

# Installing Browser Display Software

In order to render your Home Assistant dashboards in full screen on your Android tablet, you'll need an application that will render in a full screen fashion and provides additional functionality to make interacting with the dashboards easier.

There are currently three applications supported. **You need to pick ONE of the following:**

- [View Assist Companion App](./vaca.md) - Recommended. The View Assist Companion App (VACA) is an Android application and integration written by View Assist developer Mark Parker. This combination provides a simple to install means of providing both microphone input and display output but also provides tons of additional functionality. VACA creates an Home ASsistant Assist Satellite device providing even more HA native functions. Click the link for installation instructions. **BE SURE TO INSTALL thE View Assist Companion App INTEGRATION!!!\_** Skipping the installation of the VACA integration is by far the cause of most problems people have with using it with View Assist.
- [Wallpanel](./wallpanel.md) - A free Android app that provides a full screen browser and additional features.
- [Fully Kiosk](./fully-kiosk.md) - A full featured paid Android app that provides additional features not offered by Wallpanel. Features like remote management, capturing images from the webcam and more.
- [Remote Assist Display](./remote-assist-display.md) - This project provides a full screen browser with its own ability to control the views shown. Available for Android and Linux. RAD control is an alternative to the Browser Mod control used on the other devices. Browser Mod is NOT required when using Remote Assist Display

**NOTE** If you were previously using BrowserMod for control and want to allow View Assist to control your device you will need to remove BrowserMod integration and remove it from resources otherwise conflicts will exist and View Assist will not register the browser

# Installing the Lovelace Prerequisites

The View Assist dashboard and views are built using several great frontend Lovelace cards and utilities. These are easily installed via HACS. **These must be installed**

[![Image](https://img.youtube.com/vi/TIE-IgPEp8U/mqdefault.jpg)](https://www.youtube.com/watch?v=TIE-IgPEp8U)

Detailed install video:
https://youtu.be/TIE-IgPEp8U

View Assist required Lovelace cards and tools:

- layout-card
- card-mod
- button-card

For each of the three listed above do this:

- Open HACS
- Go to Frontend
- Click '+ Explore and Download Repositories'
- Search for the card to install using the name above
- Click 'Download' and 'Download' again
- Allow the reload when prompted

See the video for checking if all resources are loaded correctly. This should happen automatic but if you run into issues you will want to check these resources.
