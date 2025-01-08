---
title: Dashboard Installation
sidebar_position: 2
---

# Dashboard Installation

[![Image](https://img.youtube.com/vi/wjp0PuAlt-U/mqdefault.jpg)](https://www.youtube.com/watch?v=wjp0PuAlt-U)

Detailed install video:
https://youtu.be/wjp0PuAlt-U


* Create a new dashboard in Home Assistant by going to Settings > Dashboards
* Add Dashboard
* New dashboard from scratch
* Title dashboard "ViewAssist" and icon "mdi:glasses"
* Click Create
* Open the new dashboard, click three dots and Edit dashboard
* Click the three dots and choose "raw configuration editor"
* Copy and paste this YAML code ([link to GH raw code](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/dashboard/dashboard.yaml))
* At the top of the configuration you will need to modify this variable to match your configuration:
     * `var_assist_group`: YOUR VIEW ASSIST GROUP ENTITY (default group.viewassist_satellites)
* Click Save
* Click X to close the Edit Configuration screen
