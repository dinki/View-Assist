# Play TuneIn with Music Assistant

## Requirements

- Music Assistant server installed and integrated with Home Assistant
- Create a free account on Tune In and add some stations to your favorites on the Tune In website
- Install TuneIn Radio music provider in Music Assistant, configure, and allow time to sync
- View: [Music view](../views/music)
- The TuneIn station ID as seen in Music Assistant (see instructions for finding below)
- The recently added musicplayer_device must be added to your View Assistant device configuration as explained in the [Satellite Custom Device Configuration](https://github.com/dinki/View-Assist/wiki/View-Assist-device-configuration#satellite-custom-device-configuration) portion of the wiki. This should be a Music Assistant player device. Typically these will be named the same as your mediaplayer_device but with a \_2 on the end

## How to find Station ID

Open Music Assistant and then go to the radio page (1). Find the station you want to play and enter the text displayed EXACTLY as shown (2)

![image](https://github.com/user-attachments/assets/026e51e3-bd5c-440f-ba0e-e221a40e9f9a)

## To do

- Change name of blueprint from 'TuneIn' to 'radio' as this works with TuneIn and Radio Browser

## Changelog

| Version | Description                                          |
| ------- | ---------------------------------------------------- |
| v 1.0.3 | Bug fix plus add ability to have custom announcement |
| v 1.0.2 | Update to use condtional response                    |
| v 1.0.1 | Update to use music_assistant action                 |
| v 1.0.0 | Initial release                                      |
