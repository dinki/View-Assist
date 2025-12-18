---
title: "View Assist Actions"
sidebar_position: 5
---

# View Assist Actions

The View Assist integration provides action calls that can be used in automations. This page will list those as well as their options and usage.

## View Assist: Broadcast Event

### Description

Send a custom event

### Parameters

- event_name - The name of the event
- event_data - The event data variables to include in the event broadcast

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

- entity_id - The media player to cancel the alarm on

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

- timer_id - The id of the timer
- entity_id - Entity id of the View Assist entity
- device_id - The id of the voice satellite device to cancel all timers for
- remove_all - Cancel all timers
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

- timer_id - The id of the timer
- entity_id - Entity id of the View Assist entity
- device_id - The id of the voice satellite device to get all timers for
- name - The name of the timer

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

- download_from_repo - Download from the github repository, overwriting any existing copy
- community_view - If this should be downloaded from the community views folder
- backup_current_view - Backup yaml of view if it exists before updating

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

- device - The device to change screen on
- path - Path in dashboard view

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

- name - The name of the view

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

- entity_id - target VA satellite device
- state - the parameters to set (see example below
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

- entity_id - Entity id of the View Assist entity
- device_id - Device id of the voice satellite
- type - The type of timer - alarm, timer, reminder, command
- name - The name of the timer
- time - A spoken like time sentence

### Example

```
action: view_assist.set_timer
data:
  entity_id: sensor.viewassist_kitchen
  type: Timer
  name: egg
  time: two minutes
```

## View Assist: Snooze Timer

### Description

Snoozes an expired timer

### Parameters

- timer_id - the unique id of the timer
- time - the snooze time in minutes

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

- entity_id - The media player to play the alarm on
- media_file - Media file to use for alarm
- max_repeats (optional) - The maximun number of times to repeat the alarm media file

### Example

```
action: view_assist.sound_alarm
data:
  entity_id: media_player.android_viewassist_livingroom_wyoming
  media_file: mysound.mp3
  max_repeats: 2
```

## View Assist: Add Status Item

### Description

Adds an icon to either the launch icons or menu items.

| Parameter     | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `entity_id`   | The View Assist entity to update                                   |
| `status_item` | Single icon or list of icons to add                                |
| `menu`        | Whether to add to menu (`true`) or launch icons (`false`, default) |
| `timeout`     | Optional auto-removal timeout in seconds                           |

### Examples

```yaml
# Add a single launch icon (always visible)
action: view_assist.add_status_item
data:
  entity_id: sensor.view_assist_main
  status_item: "entity:light.lamp|lightbulb-on,lightbulb-off"
  menu: false

# Add multiple launch icons
action: view_assist.add_status_item
data:
  entity_id: sensor.view_assist_main
  status_item:
    - "entity:light.bedroom|lightbulb-on,lightbulb-off"
    - "view:camera|security"
    - "weather"
  menu: false

# Add a menu item with auto-removal after 5 minutes
action: view_assist.add_status_item
data:
  entity_id: sensor.view_assist_main
  status_item: "action:script.good_night|sleep"
  menu: true
  timeout: 300
```

## View Assist: Remove Status Item

### Description

Removes an icon from either the launch icons or menu items.

| Parameter     | Description                                                             |
| ------------- | ----------------------------------------------------------------------- |
| `entity_id`   | The View Assist entity to update                                        |
| `status_item` | Single icon or list of icons to remove                                  |
| `menu`        | Whether to remove from menu (`true`) or launch icons (`false`, default) |

### Examples

```yaml
# Remove a single launch icon
action: view_assist.remove_status_item
data:
  entity_id: sensor.view_assist_main
  status_item: "entity:light.bedroom|lightbulb"
  menu: false

# Remove multiple menu items
action: view_assist.remove_status_item
data:
  entity_id: sensor.view_assist_main
  status_item:
    - "entity:switch.fan|fan"
    - "weather"
  menu: true
```

## View Assist: Toggle Menu

### Description

Toggles the status menu visibility.

| Parameter   | Description                      |
| ----------- | -------------------------------- |
| `entity_id` | The View Assist entity to update |

### Example

```yaml
# Toggle the status menu
action: view_assist.toggle_menu
data:
  entity_id: sensor.view_assist_main
```

## View Assist: Update Versions

### Description

Forces an update of the asset versions outside of the normal 2 hour cycle

| Parameter | Description |
| --------- | ----------- |
| none      |             |

### Example

```yaml
action: view_assist.update_versions
data: {}
```

## View Assist: Load Asset

### Description

Loads/updates the dashboard, a view or a blueprint from the repo

| Parameter                | Description                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| asset class              | dashboard, views or blueprints                                                                                                                    |
| name                     | the name of the asset (as per the directory name on the repo)                                                                                     |
| download_from_repo       | (boolean) whether to load from the version on disk or pull from the repo                                                                          |
| download_from_dev_branch | (boolean) whether to load from the version on disk or pull from the development branch of the repo                                                |
| backup_current_asset     | (boolean) whether to take a copy of the currently installed version before updating. Saves in `view_assist/[asset_class]/[asset_name].saved.yaml` |

### Example

```yaml
action: view_assist.load_asset
data:
  download_from_repo: true
  download_from_dev_branch: true
  backup_current_asset: false
  asset_class: blueprints
  name: Broadcast
```

## View Assist: Save Asset

### Description

Saves an installed asset to file in `view_assist/[asset_class]/[asset_name].saved.yaml`. Does not applied to the dashboard

| Parameter   | Description            |
| ----------- | ---------------------- |
| asset class | views or blueprints    |
| name        | the asset name to save |

### Example

```yaml
action: view_assist.save_asset
data:
  asset_class: blueprints
  name: Broacast
```
