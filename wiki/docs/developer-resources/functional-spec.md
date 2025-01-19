# Functional spec

## Components
VA integration consists of two components:
- one or more HA entities, representing one or more satellite devices, such as Lenovo Thinksmart tablet
- a panel

## Guiding principles

1. Config should be as simple as possible and limit the amount of code editing required.
2. More advanced scenarios and tweaks might require code editing.
3. Satellites should be easy to set up and require minimal maintenace once set up.
4. Panel should be configurable for all satellites at once while also allowing for satellite-specific configurations.
5. Satelite specific set up is in the config flow.
6. Optional settings for satellites are in options flow.
7. Settings that are set for multiple satellites should be in the panel.

## Satellite set up and configuration
Setting up a satellite requires the following steps:
1. Satellite device hardware and software configuration
2. Requirements set up
3. Integration set up

### Configuration of the Satellite device hardware and software
This is highly specific to the sattelite device used and while we can and will provide guidance / instructions for popular devices it's impossible to describe all. We will however describe the requirements for a satellite.

### Requirements set up
Before the satellite can be configured as an entity in HA, various other components need to be set up. Their set up is out of scope for the VA integration and needs to be performed before the VA satellite entity is set up. Here's a list of components required and the options available. We will provide documentation and instructions for each.
1. *Browser mod*. Needs to be installed (hopefully in the future we will have an option that doesn't require this).
2. *Microphone device*. Available options: HassMic (preferred), StreamAssist, ...
3. *Media player device*. Available options: browsermod media player, HassMic media player, ...
4. *Music player device*. Can be the same as the media player device, so same options are available. Additional options like Music Assistant are available (and most common).

### Integration setup
The VA integration can be found in the HA integration screen and will walk the user through a series of steps (config flow) to set up the integration and a satellite. The satellite is represented as a HA sensor with attributes. If the user wants to configure multiple satellites they simply start the config flow again. One set up of the first satellite the panel is created. We will have one panel, even if there are multiple satellites set up. 

#### Config flow
These are the settings provided during config flow:
1. Type: device with display or without
2. Name: the unique name of the satellite
3. Microphone device: the entity to use as the microphone device. This devices captures the intent of the user speaking to the satellite.
4. Media player device: the entity to use as the mediaplayer for the satellite. TTS output will be sent to this media player device.
5. Music player device: the entity to use as the musicplayer for the satellite. This can be different or the same as the media player device. Will be used to play music to.
6. Display device: which entity to use to display satellite output on. Only available for satellites that are configured as type display. This should be set to the browser path entity of browser mod for the satellite.
7. Browser ID: the ID of the browser mod installation. Only available for satellites that are configured as type display. 

#### Options flow
The options flow is available after finishing the config flow for a satellite and will give the user access to the following settings so they can change these without having to delete and re-create their satellite config:
1. Type
2. Microphone device
3. Media player device
4. Music player device
5. Display device
6. Browser ID
7. Specific weather entity to use (to override weather entity configured for all satellites)

These settings are in the options flow because we don't feel like the user needs to change them that often after they are set up (principle ##5).

### What the integration set up creates
Succesfully completing at least one config flow of the integration creates the following items:
- a sensor representing each satellite. Each satellite has its own sensor entity
- a panel that hosts the views. There is only one panel and all satellites share the same panel but can have specific configurations for the views in the panel (see below).
- a group hosting all the satellites. There is only one group of satellites.
- a timer helper for each satellite. there is only one timer per satellite.

### Panel
This is the big one. The panel serves multiple purposes:
-  It's the dashboard satellites with a display will show. This will be configured automatically as part of the config flow for the satellite.
-  The dashboard consists of multiple views. The following views are provided:
    1. Clock
    2. Intent
    3. Music
    4. Camera
    5. List
    6. Locate
    7. Sports
    8. Thermostat
    9. Weather
    10. Webpage
- a settings page accessed from any view by selecting the setup icon in the top-right (icon t.b.d.). This set up page provides the following options:
- specific configurations per view
- generic configurations. These configurations are applied to all satellites and views

By default, the page showing the settings for the view that the settings page was accessed from is opened, but others can easily be accessed.
Each configuration page has a save and cancel button which applies the changes (in case of save) and closes the settings page.