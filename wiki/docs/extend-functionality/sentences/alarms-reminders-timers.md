---
title: Alarms Reminders & Timers
---

# Alarms Reminders & Timers

### Description

This custom sentence allows for an on demand call to create and list alarms, reminders and timers. While this intial version is fully functional, I do not take any responsibility if this makes you late for work, forget to buy your wife flowers, or if your eggs get overcooked. There's your warning and my escape clause!

### Usage

Use your wakeword and say things like:

- Set a timer for 2 minutes
- Start an egg time for 3 minutes
- List my timers
- Remind me to wash the dog at 3pm
- Set a reminder to take the food out of the over in 30 minutes
- Cancel my egg timer
- Set an alarm for 4pm

### Requirements

- **View**: [Alarm view](../views/alarm)

### Installation

- This blueprint is included by default in the View Assist integration.
- Find and upload a sound to play when the timer expires.
  - Any valid mp3 file should work. Place the file in /config/www/viewassist/. You may have to create the 'viewassist' subdirectory.
  - In the Alarm Sound Path blueprint field, enter either `http://your-HA-IP:your-HA-Port/local/viewassist/your-alarm.mp3` or `/local/viewassist/your-alarm.mp3`. 
  - Still need help? See the Stream Assist video where I discuss how to find these and where to upload.

### Tips

- The mp3 file is played repeatedly to create the alarm sound. When you press the dismiss button, the mp3 file will complete its current repeat before stopping, so choose a short (1-2 second) mp3 if you want the sound to stop quickly after pressing dismiss.

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
