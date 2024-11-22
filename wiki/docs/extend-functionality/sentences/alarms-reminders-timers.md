---
title: Alarms Reminders & Timers
---

# Alarms Reminders & Timers

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2FAlarms_Reminders_Timers%2Fblueprint-alarmsreminderstimers.yaml)


Detailed install video: Coming Soon!

### Description
This custom sentence allows for an on demand call to create and list alarms, reminders and timers.  While this intial version is fully functional,  I do not take any responsibility if this makes you late for work, forget to buy your wife flowers, or if your eggs get overcooked.  There's your warning and my escape clause!


### Usage
Use your wakeword and say things like:

* Set a timer for 2 minutes
* Start an egg time for 3 minutes
* List my timers
* Remind me to wash the dog at 3pm
* Set a reminder to take the food out of the over in 30 minutes
* Cancel my egg timer
* Set an alarm for 4pm

### Requirements
- **View**:  [Alarm view](../views/alarm)

### Installation

* Download and install the pyscript file (.py) found in this directory and put it in your pyscript directory.  Need help?  See the pyscript video
* Download and install the view listed above
* Find and upload a sound to play when the timer expires.  Need help?  See the Stream Assist video where I discuss how to find these and where to upload
* Install blueprint using button above and configure options
* Install the [play sound on media player](https://github.com/dinki/View-Assist/tree/main/View_Assist_scripts/Play_Sound_on_Media_Player) script.  Open the blueprint and click 'save script' button at bottom.  Keep all options the same and click 'rename' to make the script available for use
* Install the [play sound on media player repeat](https://github.com/dinki/View-Assist/tree/main/View_Assist_scripts/Play_Sound_on_Media_Player_Repeat) script.  Open the blueprint and click 'save script' button at bottom.  Keep all options the same and click 'rename' to make the script available for use

### Unfinished business

This blueprint is fully functional and it does work well.  You need to know a couple of things:

* This will not survive a restart.  The states are not persistent.  This is a big hole and I have plans to fix it.  Just know that a restart will cancel everything so don't use this for mission critical tasks just yet if you plan to restart before your timer expires
* You can only set alarms/reminders by time for today.  I will soon add the ability to add today/tomorrow/Tuesday/etc but it's not in there yet
* When you ask to list timers it will list timers, alarms, and reminders.  I will make these individual calls soon

## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.0.0 | Initial release |