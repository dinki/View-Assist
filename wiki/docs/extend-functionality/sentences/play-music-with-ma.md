# Play Music with Music Assistant

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FPlay_Music_with_Music_Assistant%2Fblueprint-playmusicwithmusicassistant.yaml)

## Requirements
  * Music Assistant server installed and integrated with Home Assistant
  * View: [Music view](../views/music)
  * The recently added musicplayer_device must be added to your View Assistant device configuration as explained in the [Satellite Custom Device Configuration](https://github.com/dinki/View-Assist/wiki/View-Assist-device-configuration#satellite-custom-device-configuration) portion of the wiki.  This should be a Music Assistant player device.  Typically these will be named the same as your mediaplayer_device but with a _2 on the end
 
## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.0.1 | Move change view to beginning of sequences and change default view values to the correct one |
| v 1.0.0 | Initial release |