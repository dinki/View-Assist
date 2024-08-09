# View Camera

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
* camera view
