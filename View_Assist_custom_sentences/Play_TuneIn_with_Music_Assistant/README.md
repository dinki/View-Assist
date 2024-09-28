# Play TuneIn with Music Assistant

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FPlay_TuneIn_with_Music_Assistant%2Fblueprint-playtuneinwithmusicassistant.yaml)

Requirements:
  * Music Assistant server installed and integrated with Home Assistant
  * Create a free account on Tune In and add some stations to your favorites on the Tune In website
  * Install TuneIn Radio music provider in Music Assistant, configure, and allow time to sync
  * View: [Music view](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/music/music.yaml)  See this [video](https://www.youtube.com/watch?v=QmWDNtikHaU) for installation procedure
  * The TuneIn station ID as seen in Music Assistant (see instructions for finding below)
  * The recently added musicplayer_device must be added to your View Assistant device configuration as explained in the [Satellite Custom Device Configuration](https://github.com/dinki/View-Assist/wiki/View-Assist-device-configuration#satellite-custom-device-configuration) portion of the wiki.  This should be a Music Assistant player device.  Typically these will be named the same as your mediaplayer_device but with a _2 on the end
## How to find Station ID

Open Music Assistant and then go to the radio page (1).  Find the station you want to play and enter the text displayed EXACTLY as shown (2)

![image](https://github.com/user-attachments/assets/026e51e3-bd5c-440f-ba0e-e221a40e9f9a)


## Change Log

v 1.0.0  Initial release
