<a href="https://www.youtube.com/watch?v=dZLcBbkZaes"><img src="https://img.youtube.com/vi/dZLcBbkZaes/mqdefault.jpg" width="60%"></a>

Detailed install video:
https://youtu.be/dZLcBbkZaes

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FBroadcast%2Fblueprint-broadcast.yaml)

This custom sentence will sound an alert sound and broadcast an audio message to all View Assist satellites that are not in do not disturb mode.  The text version of the message will appear on the screens of all View Assist satellites with displays that are not in hold mode.

This automation requires the Chime TTS extension and a TTS service.  The Google Translate TTS works well for this.  Instructions for installing below.

## Google Translate configuration
Add the following to your Home Assistant configuration.yaml file:

```
tts:
  - platform: google_translate
    service_name: google_say
```

Note that you must have at least two View Assist devices configured and in your View Assist group to use this automation
