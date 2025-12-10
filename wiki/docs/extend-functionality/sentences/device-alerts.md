---
title: Device Alerts
---

# Device Alerts

Note that this is a somewhat advanced blueprint so some patience may be required. We are always available for help on our Discord server

## Description

This blueprint is unique in comparison to other View Assist sentence blueprints. The Device Alerts blueprint does not have a voice component. It is used to do something when something else happens. This page will serve as an explanation of the options and also provide some examples. The rest is up to you. Enjoy this powerful automation creation which is hopefully easier than writing these automations from scratch.

## Usage

As mentioned, the resulting automations will provide an action on one, some or all of the View Assist satellite. The first two options allow for choosing all of the VA satellites or certain ones. Choose either all or individual or groups of VA satellites but do not do both.

The blueprint will require a `Start Alert` and an optional `End Alert`. Within each of these you will have the option to set:

- Start Sensor (mandatory) - The sensor/entity that you are monitoring for change
- Start Sensor To Condition (mandatory) - The value the start sensor to watch for (example 'on')
- Start Sensor From Condition (optional) - The value the start sensor comes from (example 'off')
- Start Wait Duration (optional) - The amount of time the `Start Sensor To Condition` state must be set before becoming true (example 'on' for 60 seconds)
- Start Icon (optional) - The View Assist icon to display in the status section. This MUST be defined in the dashboard to be usable (example 'weather') See [this wiki page](https://dinki.github.io/View-Assist/docs/view-assist-configuration/masterconfig-configuration/dashboard-options#icon-templates) for information on defining your own custom icons
- Start Speech (optional) - The speech to speak on the selected VA satellites
- Start Alert Variables (optional) - Any VA variables to be set. This can allow for doing things like setting titles, hold mode, view specific variables and just about anything you like for your VA satellite attributes. Example is prepopulated for setting values to show on the `alert` View Assist view. This can be removed if not used.
- Start View (optional) - The View Assist view to change to (example /view-assist/alert)

The `End Alert` offers similar options as the `Start Alert`. These are all optional BUT you must have a value in the `End Sensor` otherwise the automation will fail to save. This is a limitation of the Home Assistant blueprint system. We have prepopulated that field with a fake sensory `sensor.dummy` so you can either leave that as defined if you are not using the end alert functionality or set it to a sensor if you choose to have an end sensor event. If using the end sensor functionality you will need to set the `End Sensor` and `End Sensor To Condition` otherwise the whole `End Alert` definitions can be left as presented.

## Examples

Here are some ideas for automations that can be created using the Device Alerts blueprint

### Show doorbell camera for 60 seconds when button is pressed

```
    Start Sensor: binary_sensor.doorbell
    Start View: /view-assist/camera?camera=camera.doorbell_camera&timeout=60
```

### Show Teams icon when on a Teams call and remove when call ends

```
    Start Sensor: binary_sensor.beelink_isinmeeting
    Start Sensor: "on"
    Start Icon: teams
    End Sensor: binary_sensor.beelink_isinmeeting
    End Sensor To: "off"
    End Icon: teams
```

### Show the alert screen when the washer finishes

```
    Start Sensor: input_boolean.washer
    Start Sensor_to: "off"
    Start Sensor_from: "on"
    Start_Alert:
      alert_data:
        icon: mdi:washing-machine-alert
        header: Washer Status
        line1: The wash cycle has finished
        line2: Please move clothes to dryer
```

### Show the alert screen when the alarm is armed and send a different message when it is disarmed

```
    Start Sensor: alarm_control_panel.alarmo
    Start Sensor_to: armed_home
    Start Alert:
      alert_data:
        icon: mdi:home-circle
        header: Alarm Status
        line1: Armed Home
        line2: ""
    End Sensor: alarm_control_panel.alarmo
    End Sensor To: disarmed
    End Alert:
      alert_data:
        icon: mdi:home-circle
        header: Alarm Status
        line1: Disarmed
        line2: ""
```

Do you have a clever use for this blueprint? Let us know and we will include it for others!

## Requirements

- None

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
