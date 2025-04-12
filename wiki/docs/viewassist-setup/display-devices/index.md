---
sidebar_position: 4
title: "Step Three: Display Devices"
---

# Installing Browser Display Software
In order to render your Home Assistant dashboards in full screen on your Android tablet, you'll need an application that will render in a full screen fashion and provides additional functionality to make interacting with the dashboards easier. 

There are currently three applications supported.  **You need to pick ONE of the following:**
- [Remote Assist Display](./remote-assist-display.md) - Recommended.  This project provides a full screen browser with its own ability to control the views shown.  This is control is an alternative to the Browser Mod control used on the other devices.  Browser Mod is NOT required when using Remote Assist Display
- [Wallpanel + BrowserMod](./wallpanel.md) - A free Android app that provides a full screen browser and additional features.  **Requires BrowserMod**
- [Fully Kiosk + BrowserMod](./fully-kiosk.md) - A full featured paid Android app that provides additional features not offered by Wallpanel. Features like remote management, capturing images from the webcam and more.  **Requires BrowserMod**

# Installing the Lovelace Prerequisites

The View Assist dashboard and views are built using several great frontend Lovelace cards and utilities.  These are easily installed via HACS.  **These must be installed**

[![Image](https://img.youtube.com/vi/TIE-IgPEp8U/mqdefault.jpg)](https://www.youtube.com/watch?v=TIE-IgPEp8U)

Detailed install video:
https://youtu.be/TIE-IgPEp8U

View Assist required Lovelace cards and tools:
* layout-card
* card-mod   
* button-card

For each of the three listed above do this:
* Open HACS
* Go to Frontend
* Click '+ Explore and Download Repositories'
* Search for the card to install using the name above
* Click 'Download' and 'Download' again
* Allow the reload when prompted

See the video for checking if all resources are loaded correctly.  This should happen automatic but if you run into issues you will want to check these resources.