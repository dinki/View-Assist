# View Camera


[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FView_Camera%2Fblueprint-viewcamera.yaml)


This blueprint allows the user to display any camera listed in the configuration by asking assist to 'show {cameraname} camera'.  The trickiest part of the install is defining the dictionary option though it is not hard once you understand it:

```
 {"front":"camera.front_camera","doorbell":"camera.mydoorbellcamera"}
```

This is a dictionary.  The format is "what you want to call the camera by voice":"the Home Assistant camera. device" .  Additional cameras are separated by commas.  You can have as many or as little as you like but you must have at least one.  You can reuse the same camera with multiple ways to call it.  For example:

```
 {"front":"camera.front_camera","driveway":"camera.front_camera","doorbell":"camera.mydoorbellcamera"}
```

Here the user could say 'show front camera' or 'show driveway camera' and camera.front_camera would be shown for both sentences.  Note that double quotes are required for defining these dictionaries as single quotes will cause errors.

Requirements:
* [camera view](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/camera/camera.yaml)

## To do

* Only set hold mode if device called is valid and device is video capable
* Set default message for not found cameras
* Add multicamera view when Frigate card dev changes released to main

## Change Log

v 1.0.0 Initial release
