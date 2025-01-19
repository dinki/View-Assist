---
title: "Developer Resources"
sidebar_position: 6
---

## What is View Assist?

View Assist (VA) is a framework for Home Assistant (HA) Assist satellites.  Some of the core features:

- VA brings satellites with displays (view_audio) and without (audio_only) together in a group that allows for interaction between satellites.  
- VA provides preconfigured views and custom sentence automations to extend the HA Assist capabilities
- VA provides device control automations which support a variety of display related functionality

## What does a VA display look like

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
