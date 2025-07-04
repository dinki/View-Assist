---
title: Wallpanel Installation
sidebar_position: 1
---

# Wallpanel Installation and Configuration

Wallpanel is used for full screen display and is comparable to Fully Kiosk. The application is free to use and is the preferred app for View Assist use.


![https://www.youtube.com/watch?v=pFrCahUR2ZE](https://img.youtube.com/vi/pFrCahUR2ZE/mqdefault.jpg)

Detailed install video: https://www.youtube.com/watch?v=pFrCahUR2ZE

### Installation
1. Download and install the apk [from Github](https://github.com/TheTimeWalker/wallpanel-android/releases)


### Configuration
1. Open WallPanel

1. Click Get Started

1. Click the blue circle with rectangles on the bottom right to open the Wallpanel configuration.

1. Click on the Dashboard URL and enter your Home Assistant URL (format is http://192.168.1.1:8123/, where 192.168.1.1 is the IP Address of your Home Assistant instance and 8123 is the port your HA uses)

1. (optional) Change the Security Code from the default of 1234

1. Toggle the options to true/on for:
    * Open on Device Boot
    * Browser Refresh
    * Network Disconnect
    * Hardware Acceleration
    * Fullscreen
    * Prevent Screen Sleep
    * Screen Brightness (requires additional permissions to be turned on, click OK then toggle on "allow modifying system settings", then back button)
    * (optional) Dark Theme

7. (optional, potential security risk) Toggle the option to true/on for Ignore SSL Errors

8. (optional) After everything is working, you can turn off Browser Refresh and turn on Settings Transparent to have a full kiosk mode

9. Hit the back arrow

It should load the login page for Home Assistant. 

First, check the "Keep me logged in" checkbox, then enter your username and password 

:::info
It may be useful to create a unique HA user for your WallPanel devices. This allows better control of security and prevents users from making accidental changes.
:::

Special thanks to @mngarchow for the written instructions and continued support
