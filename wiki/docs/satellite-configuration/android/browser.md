---
sidebar_position: 2
title: Browser Display Software
---

# Installing Browser Display Software
In order to render your Home Assistant dashboards in full screen on your Android tablet, you'll need an application that will render in a full screen fashion and provides additional functionality to make interacting with the dashboards easier. 

There are currently two applications supported:
- [Wallpanel](#wallpanel) - Recommended. Free to Use.
- [Fully Kiosk](#fullykiosk) - $10 USD / 7.90 € per device for Plus features like remote management, capturing images from the webcam, etc.

---

## Wallpanel {#wallpanel}
Wallpanel is used for full screen display and is comparable to Fully Kiosk. The application is free to use and is the preferred app for View Assist use.


![https://www.youtube.com/watch?v=pFrCahUR2ZE](https://img.youtube.com/vi/pFrCahUR2ZE/mqdefault.jpg)

Detailed install video: https://www.youtube.com/watch?v=pFrCahUR2ZE

### Installation
1. Download and install the app on the [Google Play Store](https://play.google.com/store/search?q=wallpanel&c=apps)


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

---

## Fully Kiosk {#fullykiosk}
The free version of the application will work for some functions but will display a watermark.  This is great for testing but for production you will more than likely want to support the developer by purchasing a license.  Money well spent.  Settings labeled (PLUS) require the license.

### Installation

Download and install the app via the [Google Play Store](https://play.google.com/store/apps/details?id=de.ozerov.fully)

### Configuration

#### Web Content Settings -> 

  * Set 'Start URL' to your local HA server by name or your server address  (eg http://homeassistant.local:8123 or http://192.168.0.23:8123)
  * Set 'Username' to your HA username
  * Set 'Password' to your HA password

  
#### Advanced Web Settings ->

  * Turn on 'Ignore SSL Errors'  You may not need to do this but my old tablet did show notifications when trying to show Wikipedia images
  * Change color of 'Default Webview Background Color' to black or your favorite color

  
#### Universal Launcher ->

  * Applications to Run on Start in Background (PLUS) choose 'Ip Webcam'
  
#### Remote Administration (PLUS) ->

  * Turn on 'Enable Remote Administration'   This is needed to expose FK media player to Music Assistant addon
 
