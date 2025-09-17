# View Camera

This blueprint allows the user to display any camera listed in the configuration by asking assist to 'show \{cameraname\} camera'. The trickiest part of the install is defining the dictionary option though it is not hard once you understand it:

```
 camera.doorbell:
  - doorbell
  - door
camera.driveway:
  - driveway
```

This is a dictionary. The format is the Home Assistant device name followed by the names associated with that camera . Additional cameras can be added in a similar fashion as the example. You can have as many or as little as you like but you must have at least one.

Additionally, hold mode timeout is available. This will allow you to set a value for the return to home screen for a set time or indefinitely stay on the camera view screen by using a timeout of zero seconds

## Requirements

Nothing additional

## Changelog

| Version | Description                |
| ------- | -------------------------- |
| v 2.0.0 | Major improvements by Flab |
| v 1.0.0 | Initial release            |