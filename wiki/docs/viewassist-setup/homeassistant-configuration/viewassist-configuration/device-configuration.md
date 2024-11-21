---
title: Device Configuration
sidebar_position: 1
---

# Device Configuration 


View Assist devices are created using custom template sensors. These devices contain important information like browser mod ID, media_player device, microphone device, and timer device.  Additionally this configuration sets the attributes needed for different modes, data to displayed and more. These attributes are consumed by control automations and display views.

[![Image](https://img.youtube.com/vi/5RQvzEFfwuY/mqdefault.jpg)](https://www.youtube.com/watch?v=5RQvzEFfwuY)

Detailed install video:
https://youtu.be/5RQvzEFfwuY

:::warning
An error exists in the video where I do not configure the browser_id attribute.  I have corrected the code below but do know that you must input this value.
:::
---
## Create Timer Helper

:::info
Note that these steps are only necessary if using View Assist with video enabled satellites.  It is not necessary to install these for voice only satellites.
:::

Each `view_audio` or `view_only` View Assist device needs a timer helper that allows the control automation to reset the display to a default state. If you are using an `audio_only` device you can skip this step.

1. In Home Assistant click on **Settings*- in the sidebar
1. Click on **Devices & Services**
1. Click on **Helpers*- at the top of the screen
1. Click the **+ Create Helper*- button in bottom right corner 
1. Scroll down and select **Timer**
1. Give this a meaningful name such as `va_livingroom`
1. Choose an appropriate icon such as `mdi:clock-digital`
1. Click the **Restore?*- checkbox.
1. Click **Create**

## Satellite Custom Device Configuration

:::info
Note that these steps must be taken for all View Assist satellites.  Choose the correct configuration based on type.  View Assist satellites with screens must use the view_audio type while voice only satellites must use the audio_only configuration
:::

Each View Assist device must have its own configuration in Home Assistant. This allows for setting properties for each device that may have a unique condition for that device (eg night mode for a device in a dark room).  These devices are set up in YAML as a template device in `configuration.yaml`.  When setting up more than one device, you'll duplicate everything from the `-name:` line and below for each device you are configuring.  The Home Assistant service must be restarted any time a change is made to the `configuration.yaml` file. 

### Satellites with displays (view_audio) example:
```yaml
template:
  - sensor:
    - name: ViewAssist_livingroom
      state: ""
      attributes:
        type: view_audio
        mic_device: "sensor.streamassist_livingroom_stt" 
        mediaplayer_device: "media_player.browsermod_livingroom" 
        display_device: "sensor.browsermod_livingroom_browser_path" 
        browser_id: "ViewAssist-livingroom"
        timer_device: "timer.viewassist-livingroom" 
        view_timeout: "20"
        mode: "normal"
        title: ""
        message: ""
        message_font_size: "3vw"
        image: ""
        timer: ""
        alarm: "idle"
        cycle_view: ""
        do_not_disturb: false
```

### Voice Only Satellites (audio_only) example:
```yaml
template:
  - sensor:
    - name: ViewAssist_diningroom
      state: ""
      attributes:
        type: audio_only
        mic_device: "" 
        mediaplayer_device: "" 
        display_device: "" 
        browser_id: ""
        timer_device: "" 
        view_timeout: "20"
        mode: "normal"
        title: ""
        message: ""
        message_font_size: "3vw"
        image: ""
        timer: ""
        alarm: "idle"
        cycle_view: ""
        do_not_disturb: false
```

### View Assist Config Definitions:

<details>
    <summary>User Defined</summary>
    - **name:** Device name (eg ViewAssist-livingroom)
    - **type:**  Used to determine a/v capabilities
        - Values: `view_audio`, `view_only`, `audio_only` 
        - Default: `view_audio`
    - **mic_device:**  Used to assign microphone to View Assist device
    - **mediaplayer_device:** Used to assign the media player used for View Assist audio playback
    - **browser_id:** Used to assign the browser being used by Browsermod.
        - This will match the name you give the device in your Browsermod configuration. Capitalization matters!
    - **timer_device:** Used to assign the timer helper device used for screen time outs
    - **display_device:** Used to determine the correct Browser Mod instance to use for display
    - **view_timeout:** Amount of time (seconds) before switching views as controlled by mode
        - Default: 20
</details>
<details>
    <summary>Default values (do not change)</summary>
    - **state:** Required 
    - **mode:** Used to control actions based on conditions
        - Values: `normal`, `music`, `night`, `hold`, `cycle`
        - Default: `normal`
    - **title:** Text for displaying title of multiuse cards
    - **message:** Blob text for displaying to informational views
    - **message_font_size:** Text containing size of font to be used in message for informational views 
        - Default: `3vw`
    - **image:** Text containing image path for display on informational views
    - **alarm:** Used to trigger alarm sound and display
        - Values: `idle`, `alarming`
        - Default: `idle`
    - **cycle_view:** List containing view names to cycle through using view_timeout when in `cycle` mode
        - must be in Python list format eg. `[ 'weather', 'frontcamera' ]`
    - **dnd:** Do not disturb mode.  Do not broadcast or play sounds when in DND mode
        - Default: `false`
</details>

## View Assist Satellite Group
A group containing all View Assist Satellite devices (eg group.viewassist_satellites) must be created and all VA Satellite devices must be added to this group.  This group **MUST** be added to the `configuration.yaml` file similar to the View Assist device configuration below:  

```
group:
  viewassist_satellites:
    name: View Assist Satellites
    entities:
      - sensor.viewassist_livingroom
      - sensor.viewassist_kitchen
      - sensor.viewassist_diningroom
```
:::warning
Dashes in template sensor and device names will be replaced by underscores by Home Assistant.  This has been shown to be problematic so it is advised to not use dashes at all to avoid headaches.
:::


:::warning
- The group configuration must be reloaded after any edits by way of Home Assistant restart.
- Do not create this group as helper from the Home Assistant GUI.  It will not work and you will have problems.
:::

## Example configuration

Here is the example configuration.  You can copy paste this into your configuration.yaml file, modify the values to those of your satellite sensors and timer, save the file and then restart Home Assistant for the configuration to be loaded.  You will repeat the sensor definition for any additional satellites.  Copy starting from `- sensor:` to the end of the attributes.  All View Assist satellites must be added to the View Assist Satellite group as described above.

[Example device configuration](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20device%20configuration/device_config_example.yaml)
