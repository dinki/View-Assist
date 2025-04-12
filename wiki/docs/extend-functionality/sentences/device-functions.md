# Device Functions

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FDevice_Functions%2Fblueprint-devicefunctions.yaml)

This blueprint will contain device specific functions.  Current functions include:

* Repeat the last spoken text to speech from that device
* Set the different modes for the satellite device
* Change views by voice
* Adjust volume by level
* Adjust volume by step
* Mute/Unmute volume
* Stop music playback and return to normal mode
* Pause playback
* Next song
* Adjust music volume by level
* Adjust music volume by step
* Mute/Unmute music

Requires View Assist Control automation v1.2.0 or greater

## To do

* Add voice command to set view timeout
* Add rewind/fast forward XX seconds/minutes, previous/restart track
* query what song/media is playing by voice
* Allow for 'stop' only to end playing media
* Add 'move to [area]' to move music playback from one satellite to another


## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.4.0 | Add more music specific functions |
| v 1.3.0 | Add additional functions pause, next, additional |
| v 1.2.2 | Stop music stops music player device and expires timer to go back to home screen quicker |
| v 1.2.1 | Add volume control and stop music (Thanks @jimmyjamesbob) |
| v 1.2.0 | Add view functionality |
| v 1.1.0 | Add mode functionality |
| v 1.0.0 | Initial release |
