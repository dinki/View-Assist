---
title: Browser Control
sidebar_position: 4
---

In order to control your Home Assistant dashboards you'll need an application that will allow for sending messages to make view changes.  You will want to pick one of the supported applications below:

- [Remote Assist Display](#rad) - Recommended.  This project is meant to be an alternative to browser_mod for building dashboards controllable from Home Assistant, specifically for use with ViewAssist
- [Browser Mod](#browsermod)

# Remote Assist Display {#rad}

This project is meant to be an alternative to browser_mod for building dashboards controllable from Home Assistant, specifically for use with ViewAssist.  This will allow for both display and control.  You do not need to install Browsermod if you choose to use RAD.

### Installation

See the [install notes here](https://github.com/michelle-avery/remote-assist-display)

# Browser Mod {#browsermod}
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

![](./bm1.png)



You should see device information similar to the screenshot below.  Note the new media player device provided by Fully Kiosk.


![](./bm2.png)

---------

# Configuration

Browser Mod allows for hiding the default Home Assistant side and top menus allowing us to have a full screen experience.  After [setting up your View Assist dashboard](https://github.com/dinki/View-Assist/wiki/Lovelace-card-views#creating-a-new-dashboard-and-views), go back to Browser Mod from the sidebar menu.


![](./bm3.png)


Scroll down to Frontend Settings (1), and then expand the 'Hide sidebar' pulldown (2), click '+ Add Browser Setting', select the Fully Kiosk device you are setting up and turn 'Hide Sidebar' switch to on.  Repeat the same process for the 'Hide header' section.  Open the 'Default Dashboard' and set it to the dashboard you've created with your View Assist views.  This will ensure that the correct dashboard is displayed when booting the device.
