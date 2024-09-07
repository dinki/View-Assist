---
title: Browser Mod
sidebar_position: 1
---

# Browser Mod
Browser Mod 2 custom integration provides several key pieces of functionality for an Android Tablet Satellite:
  - Provides media player entity for voice response
  - Hides Header and Sidebar from tablet display
  - Handles service calls to change which dashboard view is displayed

## Installation

[![Image](https://img.youtube.com/vi/7UOfP5JjxFY/mqdefault.jpg)](https://www.youtube.com/watch?v=7UOfP5JjxFY)

Detailed install video:
https://www.youtube.com/watch?v=7UOfP5JjxFY

Please follow the steps for installation here:
https://github.com/thomasloven/hass-browser_mod#installation-instructions


:::danger[Restart Required]
Please remember you must restart Home Assistant after installing Browser Mod
:::

### Validate Installation
Before continuing, ensure that your tablet satellite is recognized:
1. Visit your Home Assistant URL via your Browser applications of choice (Wallpanel or Fully Kiosk) 
1. Find and tap on Browser Mod in the sidebar.
1. Next, click on the icon (2) next to your registered device

![image](https://github.com/dinki/View-Assist/assets/2521542/589e5e0e-e79a-46ec-9028-24bd70fd6755)



You should see device information similar to the screenshot below.  Note the new media player device provided by Fully Kiosk.


![image](https://github.com/dinki/View-Assist/assets/2521542/9dbaaba8-86f8-4e92-b4ba-5d2a77c6d161)

---------

# Configuration

Browser Mod allows for hiding the default Home Assistant side and top menus allowing us to have a full screen experience.  After [setting up your View Assist dashboard](https://github.com/dinki/View-Assist/wiki/Lovelace-card-views#creating-a-new-dashboard-and-views), go back to Browser Mod from the sidebar menu.


![image](https://github.com/dinki/View-Assist/assets/2521542/b383e227-161c-497b-b8e8-1dfbc5365504)


Scroll down to Frontend Settings (1), and then expand the 'Hide sidebar' pulldown (2), click '+ Add Browser Setting', select the Fully Kiosk device you are setting up and turn 'Hide Sidebar' switch to on.  Repeat the same process for the 'Hide header' section.  Open the 'Default Dashboard' and set it to the dashboard you've created with your View Assist views.  This will ensure that the correct dashboard is displayed when booting the device.
