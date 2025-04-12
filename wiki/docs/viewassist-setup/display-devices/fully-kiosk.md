---
title: Fully Kiosk Installation
sidebar_position: 2
---

# Fully Kiosk Installation and configuration

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
 