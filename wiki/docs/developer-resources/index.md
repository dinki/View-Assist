---
title: "Developer Resources"
sidebar_position: 6
---

## What is View Assist?

View Assist (VA) is a framework for Home Assistant (HA) Assist satellites.  Some of the core features:

- VA brings satellites with displays (view_audio) and without (audio_only) together in a group that allows for interaction between satellites.  
- VA provides preconfigured views and custom sentence automations to extend the HA Assist capabilities
- VA provides device control automations which support a variety of display related functionality

## What does a VA automation flow look like

A normal VA custom sentence is handled like this:

- User makes a request using the trigger for a custom sentence like "How's the weather"
- The custom sentence blueprint identifies the keyword and triggers the automation
- VA attempts to determine which device is being used (described later) and sets variables for the VA device and that devices attributes like mediaplayer_device, musicplayer_device, and display_device
- The automation will then do specialized tasks associated with the custom sentence.  Some examples would be setting the title text in the top left corner or setting device entities to show (like camera.doorbell).  This is done using the set_state.py action call
- VA may change the displayed view by making an action call to the BrowserMod (BM) action navigate.
- VA control automation watches for view changes.  When this happens, the VA device starts the associated timer
- VA will often give audio feedback
- When the timer expires VA will call the BM navigate action call to send the display back to a view.  This view is based on the mode setting.  Currently, if mode is set to normal, the displayed view will be the default view which is commonly set to the clock view.  If mode is set to music then the displayed view will be the configured view for music

## What are VA modes?

VA modes control how VA acts and looks.  These modes can be extended.  Currently these are the modes available:

- Normal - This mode is the default.  No icon is shown to indicate it is active.  Behavior is described above
- Music - Music mode is set by automations using music playback.  No icon is shown to indicate it is active.  Behavior is described above
- Hold - Hold mode is set by taping an open area on any view or by automation.  A hand icon is shown when it is active.  Hold mode prevents the timer expiring from changing the view.  This is useful when wanting to interact with a view for longer than the timeout.  An example would be calling for a security camera to be displayed and to leave it on the screen indefinitely.  Leaving hold mode can be done by taping the hand icon, use a voice command from the device functions blueprint to change modes, or by automation
- Cycle - Cycle view is set by voice using device functions blueprint to change modes or by automation.  Icon shown is arrows in a circle.  Cycle mode will cycle through a list of views set in the device attributes cycle.  The automation will use the VA device's timer to control the time that each view is displayed.  The views will continue to loop until cycle mode is exited by clicking the icon to return to normal mode or by automation
- Night - Night mode is somewhat experimental.  It is set by voice using device functions blueprint to change modes or by automation.  When in night mode the default clock screen dims to a low level that still allows it to be visible in a very dark room but also providing a means to not have a very bright light.  Additional function is planned for this mode but not implemented
- Do not disturb (DND) - Do not disturb is set by voice using device functions blueprint to change modes or by automation.  Icon shown is circle with rectangle in the middle.  Do not disturb is not exactly a mode but serves the function of preventing broadcast messages from sounding.  DND is its own attribute so it can be used in conjunction with the modes listed above.  Leaving DND can be done by taping the icon, by voice command from the device functions blueprint, or by automation

## What are some of the default actions for the VA dashboard?

The VA dashboard is built on custom button card for most elements.  This allows for great flexibility in that these items as well as the view itself can be used to trigger action calls using single tap, double tap, and hold screen interactions.  Dashboard level default actions for all views include:

- Single tap turns on `hold` mode
- Long press mutes the VA device

## How does VA determine which VA device is requesting?

VA must determine which device is being used for a request.  This is done the same in each custom sentence blueprint.  This block of code is used in each blueprint:

```
      target_satellite_device: |-
        {% for sat in expand(group_entity) %}
          {% if device_id(sat.attributes.mic_device)  == trigger.device_id %}
            {{ sat.entity_id }}
          {% endif %}
        {% endfor %}
      target_display_device: "{{ device_id(state_attr(target_satellite_device, 'display_device')) }}"
      target_mediaplayer_device: "{{ state_attr(target_satellite_device, 'mediaplayer_device') }}"
      target_satellite_device_type: "{{ state_attr(target_satellite_device, 'type') }}"
```

target_satellite_device is set by looking through all members of the satellite group (normally group.view_assist) and looking for a match of the automation's trigger.device_id and the microphone attribute of each VA device in the group.  Once the target_satellite_device is set, other attributes like target_mediaplayer_device and target_satellite_device can be derived and set.

## How are VA status and launch icons defined?

VA provides a method for providing both status and launch icons in the top right side of the view area.  These icons are custom button elements that can be defined in the [icon template](https://github.com/dinki/View-Assist/blob/main/View%20Assist%20dashboard%20and%20views/dashboard/dashboard.yaml#L512) portion of the dashboard.  These custom button icons follow the same flexibility for adding actions based on single and double tape as well as long press.  Aside from the built in VA functionality, the user is free to create these to fire services based on the type of press.  Here is an example for creating a weather icon that when single pressed will change views to the `weather` view using the `navigate` service:

```
  weather:
    type: custom:button-card
    template: icon_template
    icon: mdi:weather-sunny
    tap_action:
      action: navigate
      navigation_path: weather
```

The user has multiple ways to use this icon.  The first is through automation where the icon is added to the `status_icons` attribute.  The other is to set this as a launch icon.  Launch icons are always shown as they are permanent members of the `status_icons` attribute as a list element.  This is set in the control automation for each device.  An example configuraton for the weather example would be `['weather']` .  Additional launch icons can be set using the list separating using commas as per the standard Python list format.

## How are VA device attributes set

VA is not yet an integration so something is needed to set and create attributes.  The [set_state.py](https://dinki.github.io/View-Assist/docs/viewassist-setup/homeassistant-configuration/viewassist-configuration/control-automations#view-assist-device-control-through-python-set_state) Python script is used for setting these attributes.  This script will either update attribute values or create and set attribute values if the attribute does not exist already.  An example of use:

```
  - service: python_script.set_state
    data:
      entity_id: sensor.viewassist_office
      title: Announcement
      message_font_size: 4vw
      message: '{{trigger.slots.message | capitalize}}'
```

In the example, the `entity_id` is the VA device and the remaining are attributes to set.

## What variables are set in the VA dashboard?

VA dashboard sets variables for use in views as well as other display functions.  These are defined in the dashboard `variable_template`.  Some of these variables include:

- var_assistsat_entity_font_style - font style for the VA device
- var_assistsat_entity_weather_entity -  weather entity for the VA device
- var_assistsat_entity_status_icons_size - size of icons in the status area 
- var_assistsat_entity_use_24_hour_time - boolean for use 24 hour time or am/pm
- default_satellite - this is set if the device cannot be determined.  This allows for dev work to be done on a nonVA device
- var_current_time - current time
- var_current_time_alt - current time in alternate format
- var_date_short - current date in short format (Sun, Jan 19)
- var_date_long - current date in long format (Sunday, January 19, 2025)
- var_assistsat_entity - the VA device associated with this display device
- var_assisting - boolean that is true when current device wake word detected and listening
- var_assisting_text - Text to show when using blur pop up (example "How may I assist?")
- var_assist_prompt - The style of assist prompt to show (example blur popup or flashing bar)
- var_mic_switch - The device used to mute the microphone for this VA device
- var_mediaplayer_device - The mediaplayer for this VA device
- var_mediaplayer_mute - The status of microphone (true is muted false is not muted)
- var_title - The text for the title to display in top left corner of view
- var_message - The text for the main section of the view (example info view)
- var_image - Image to be used for the view
- var_font_size - Font size to use for text in the main section of the view
- var_weather_temperature - current temperature
- var_weather_icon - current weather condition

  
## How are VA attributes handled in views?

VA uses views which are based on custom button card.  Custom button card uses javascript.  Here is an example of how VA attributes can be set in views:

```
variables:
  cameracardversion: 1.0.1
  var_camera: >-
    [[[ try {return
    hass.states[variables.var_assistsat_entity].attributes.camera} catch {
    return  ""}]]]
```
then later these can be used in the view.  Here the camera device stored in the variable is being used to show the name of the camera in the `title` section of the VA view:

```
custom_fields:
  title: >-
    [[[ try {return hass.states[variables.var_camera].attributes.friendly_name}
    catch {return ""}]]]
```
In the above example, the `camera` attribute is being set using the `var_assistsat_entity` value that is set by the variable template of the dashboard.  This allows for reusing the same view for any camera entity. This adds great flexibility for VA views

## What are the sections of a 'standard' VA view

The VA view format has several sections by default.  These should be adhered to where possible when creating views so that a consistent look and feel can be achived.  Here are the default areas and their use:

- Title - Top left portion of the screen.  This is typically used to define the name of the view or provide other data
- Status - Top right port of the screen.  This is used to display status and launch icons
- Message - This is the main focus of the view.  It covers the entire view with the Title, Status, and Assist sections overlaying it at higher z-index levels
- Assist - The visual indicator that assist is in progress.  
## 
