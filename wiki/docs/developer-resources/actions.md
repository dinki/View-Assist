---
title: "View Assist Actions"
sidebar_position: 5
---

# View Assist Actions

The View Assist integration provides action calls that can be used in automations.  This page will list those as well as their options and usage.



## View Assist: Broadcast Event
### Description 
Send a custom event

### Parameters
* event_name - The name of the event	  
* event_data - The event data variables to include in the event broadcast
### Example
```
action: view_assist.broadcast_event
data:
  event_name: my event
  event_data: my data
```

## View Assist: Cancel sound alarm
### Description 
Cancel a sounding alarm

### Parameters
* entity_id - The media player to cancel the alarm on
### Example
```
action: view_assist.cancel_sound_alarm
data:
  entity_id: media_player.android_viewassist_livingroom_wyoming
```

## View Assist: Cancel timer
### Description 
Cancel running timer

### Parameters
* timer_id - The id of the timer	  
* entity_id - Entity id of the View Assist entity	  
* device_id - The id of the voice satellite device to cancel all timers for	  
* remove_all - Cancel all timers
Examples:
```
action: view_assist.cancel_timer
data:
  timer_id: egg
  entity_id: sensor.viewassist_kitchen
```

## View Assist: Get Timers
### Description

Get all timers or by timer id or device id

### Parameters
* timer_id - The id of the timer	  
* entity_id - Entity id of the View Assist entity	  
* device_id - The id of the voice satellite device to get all timers for	  
* name - The name of the timer

### Example
```
action: view_assist.get_timers
data:
  entity_id: sensor.viewassist_livingroom
```
## View Assist: Load View
### Description

Install a view from the View Assist views directory or repository

Paramters:
* download_from_repo - Download from the github repository, overwriting any existing copy	  
* community_view - If this should be downloaded from the community views folder	  
* backup_current_view - Backup yaml of view if it exists before updating

### Example
```
action: view_assist.load_view
data:
  download_from_repo: true
  backup_current_view: true
  name: clock
```
## View Assist: Navigate to a view
### Description

Command device to navigate to a certain view

### Parameters
* device - The device to change screen on	
* path - Path in dashboard view

### Example
```
action: view_assist.navigate
data:
  device: sensor.viewassist_livingroom
  path: /view-assist/weather
```
## View Assist: Save View
### Description 

Save a view to the View Assist views directory

### Parameters
* name - The name of the view

### Example
```
action: view_assist.save_view
data:
  name: info
```

## View Assist: Set View Assist master config
### Description

To set master config parameters that apply across all View Assist devices

### Parameters
Any supported key/value pair.
Currently only supports show_date: true/false

### Example
```
action: view_assist.set_master_config
data:
  show_date: true
```
## View Assist: Set state or attributes
### Description

Set state or attributes of View Assist entity

### Parameters
* entity_id - target VA satellite device
* state - the parameters to set (see example below
)
### Example
```
action: view_assist.set_state
target:
  entity_id: sensor.viewassist_kitchen
data:
  title: My title
  message: Hi there
```
## View Assist: Set a timer
### Description

Set an alarm, timer or reminder

### Parameters
* entity_id - Entity id of the View Assist entity	  
* device_id - Device id of the voice satellite	  
* type - The type of timer - alarm, timer, reminder, command	  
* name - The name of the timer	  
* time - A spoken like time sentence

### Example
```
action: view_assist.set_timer
data:
  entity_id: sensor.viewassist_kitchen
  type: Timer
  name: egg
  time: two minutes
```

## View Assist: snooze_timer
### Description 

Snoozes an expired timer 

### Parameters
* timer_id - the unique id of the timer
* time - the snooze time in minutes


### Example
```
action: view_assist.snooze_timer
data:
  timer_id: 01JR5TTJPM23CDRS91SG2R2CSE
  time: 5
```

## View Assist: Sound alarm
### Description 

Sound alarm on a media device with an attempt to restore any already playing media

### Parameters
* entity_id - The media player to play the alarm on	  
* media_file - Media file to use for alarm	  
* max_repeats (optional) - The maximun number of times to repeat the alarm media file
### Example
```
action: view_assist.sound_alarm
data:
  entity_id: media_player.android_viewassist_livingroom_wyoming
  media_file: mysound.mp3
  max_repeats: 2
  ``` 

