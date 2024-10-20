---
title: Extended Device Controls
---
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FVACC_Extended_Device_Control-Display_and_Audio%2Fblueprint-vacc-extendeddevicecontrol.yaml)

This blueprint enhances the control of View Assist device displays and audio playback. This is a community contribution authored by user [Flight-Lab (Github)](https://github.com/Flight-Lab)/flab (Discord).  Support can be obtained through the View Assist [Discord server](https://discord.com/channels/1241796965344481440/1295408431498395709) or the [discussion group](https://github.com/dinki/View-Assist/discussions) on Github.  Please tag the author in your message.

---

:::info[Note]    
> * Each device requires its own automation.        
> * Most features require modifications to the View Assist device configuration YAML file.        
> * All features are opt-in. 
:::
---

## Summary of Optional Features:
- Automatically decrease music volume when triggered by wake-word detection or the broadcast automation, and restore
    music volume when TTS ends.
  - option to gradually increase volume
- Play a custom sound when wake word is detected.
- Play a custom sound when STT detects silence.
- Switch to music mode when `musicplayer_device` is playing.
- Revert to normal mode when `musicplayer_device` is idle for specified duration.
 
<details>
<summary>Blueprint Input Page Screenshot:</summary>
    
![VACC-EDC-1](https://github.com/user-attachments/assets/f0461fe4-73fe-4ef9-9c07-1859dd171ea1)

</details>

---

## Features Requiring No Changes to Stock View Assist Device Configuration:
- **Assist Audio Feedback:**
    - Play a custom sound when wake word is detected (set Stream Assist `STT start media` to `null` if using this feature).
    - Play a custom sound when STT detects silence (sound is not played if Music Duck is activated, as the volume returning to normal signals the end of listening).

---

## Features Requiring Configuration Changes:
- **Home Assistant Startup:**
    - Fully Kiosk Browser automatically loads the start URL on server startup.  
    - Requires setting `fkb_device:` in the config file, which should match the device name in the Fully Kiosk Browser integration.      (e.g., `fkb_device: "pyramid"`)

---

## Features Requiring Separate Media Players:
For the following features, separate media players must be defined for `mediaplayer_device` and `musicplayer_device` in the config:
- **Auto Music Mode:**
    - Switches to music mode and navigates to the music view when `musicplayer_device` starts playing. This applies even when playback starts from any sources other than just voice commands.
- **Music Mode Timeout:**
    - Automatically returns to normal mode and the home page after a user-defined period of inactivity in music playback.
- **Music Duck:**
    - Lowers the music volume (by a user-defined percentage of the current volume) when triggered by a wake word or broadcast, and restores the original volume when TTS ends.
    - **Volume Step:**
        - Gradually increase volume after ducking for a smoother experience. Step size and time between steps are both user selectable variables.

> [!IMPORTANT]  
> These features require stable and reliable state changes between idle and playing for both `mediaplayer_device` and `musicplayer_device`. Ensure that the media players are consistently available.

## Recommended Media Players:
* **musicplayer_device:** [Snapcast](https://play.google.com/store/apps/details?id=de.badaix.snapcast&hl=en_US) (exposed via Music Assistant) **FREE**
* **mediaplayer_device:** [AirReceiver](https://play.google.com/store/apps/details?id=com.softmedia.receiver&hl=en_US) audio (exposed via Music Assistant) **$2.99**
<details>

<summary>AirReceiver Setup Instructions:</summary>

1) In AirReceiver settings, make sure both Airplay <sub>IOS Media Receiver</sub> and AirTunes Audio <sub>AirPort Express Speaker</sub> are selected. The media_player entity we want to use is only made when both of these are checked.        
(You do not need the other options selected for this but they will not harm anything if you choose to. I do, however, recommend unchecking them as they will create even more media player entities. One even creates a media server.)

2) Scroll down to "Advanced Settings" and set "AirTunes Audio Latency (ms)" to 0.

3) Check AirTunes UI [✓]

The media player entity we want to use will be created by the Music Assistant integration and will be called `media_player.lenovostarview_(last 3 digits of device ip)_audio`          
e.g. `media_player.lenovostarview_180_audio`         
This player operates independently of the device's system volume, similar to Snapcast.

</details>

<details>

<summary>Other Confirmed Working Media Players:</summary>

* [Fully Kiosk Browser](https://play.google.com/store/apps/details?id=de.ozerov.fully&hl=en_US) media player (exposed via Music Assistant)
    > [!WARNING]
    > Only use the media player exposed by Music Assistant; others may become unavailable or fail to trigger actions.
  - There may be a delay between state changes and actual audio playback (1-2 seconds for both start and end of playback).


</details>

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://gist.github.com/Flight-Lab/6ddb640f756791d59b6fd9be93375eee)

<!-- 
notes for future edits:
The general concept is to work like an audio mixer. Each channel is individually controllable and can be played at the same time as any of the other channels. This enables you to do something wild like playing music while an alarm rings and assist tells you what the alarm is for, or something more controlled like having your music lower in volume as the alarm increases in volume.  
This also lets you set permanant default levels to each channel or mute certain functions while keeping others enabled.
-->

<!--

ADB instructions

Display Brightness control using ADB

Bring Wall Panel features up to parity with FKB

soundplayer_device

-->

## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.0.2 | Updates to blueprint inputs & descriptions |
| v 1.0.1 | Add option to gradually increase volume after ducking |
| v 1.0.0 | Initial release |
