---
title: Control Automations
sidebar_position: 3
---

# Control Automations

:::info
Note that this entire section is only necessary if using View Assist with video enabled satellites.  It is not necessary to install these for voice only satellites.
:::

View Assist is controlled using core control automations per view device.  Other automations control things like alarms and reminders.  This page details the installation and configuration of some of these automations

## Installation

### View Assist device control through Python set_state
The View Assist satellite devices hold data and settings.  These devices and their attributes are updated using a python script called set_state .  This will involve file manipulation so if you need help you can watch this [video for installing file editor addon](https://www.youtube.com/watch?v=ncKWaLpJ1DQ) in HASSOS.  Here is how to install this python script for use with View Assist

[![Image](https://img.youtube.com/vi/iDJH2bn_Wao/mqdefault.jpg)](https://www.youtube.com/watch?v=iDJH2bn_Wao)

Detailed install video:
https://youtu.be/iDJH2bn_Wao


* Download the set_state.py by right clicking this link and choose 'save link as':   <a id="raw-url" href="https://raw.githubusercontent.com/xannor/hass_py_set_state/master/python_scripts/set_state.py">set_state.py</a>
* Open the configuration.yaml file located in the 'homeassistant' config directory in a file editor
* Add a line to the bottom of the configuration file containing ```python_script:``` and save the file
* Go back into file editor and create a new folder in the config directory called ```python_scripts```
* Find that new folder and click it to enter
* Use the upload file option and upload the 'set_state.py' file into the 'python_scripts' folder you created
* Restart Home Assistant
* Check that the service is installed by going to Developer Tools -> Services and search for 'set_state'.  You should see the service listed in the results as 'Python Scripts: set_state'

Note that for HASSOS users the configuration folder shows up as ```homeassistant``` where other installs have this defined as ```/config```

For more information see the set_state Github page at: https://github.com/xannor/hass_py_set_state

### Per device display control
The View Assist display satellites have different modes for how screens are shown on the device and for how long.  This behavior is controlled by an automation.  Each View Assist visual device will need its own control automation.

[![Image](https://img.youtube.com/vi/Vrm4TCotEqA/mqdefault.jpg)](https://www.youtube.com/watch?v=Vrm4TCotEqA)

Detailed install video:
https://youtu.be/Vrm4TCotEqA
  
These are the configuration parameters needed for configuration:
* Satellite -The View Assist device entity to control (example sensor.viewassist_living_room)
* Display Device - The browsermod display device used by View Assist (example sensor.browsermod_livingroom_browser_path)
* Timer - The associated timer device entity for the satellite (example timer.viewassist_living_room)
* Dashboard - The base dashboard for View Assist (default /dashboard-viewassist/)
* Default Home screen - The screen to return to after timeout (default /dashboard-viewassist/clock)
* Unmute Mic - Unmute microphone on HA start/restart. This is helpful for Stream Assist devices which default to muted on HA start
* Mic device - The microphone entity to unmute on HA start/restart. (example switch.viewassist_living_room_mic)  Only needed if Unmute Mic option is turned on


Below is the blueprint that will configure these automations for each device.  Click the link to import the blueprint:


[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_control_automations%2Fblueprint-devicecontrol.yaml)

After importing, click on the newly imported blueprint and set the configuration options as detailed above.  Hit save to write out an automation based on that blueprint.  Change the word 'template' in the name to your device name so it can be unique and identifiable.

