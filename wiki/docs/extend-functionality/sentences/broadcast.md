---
title: Broadcast
---

# Broadcast

[![Image](https://img.youtube.com/vi/dZLcBbkZaes/mqdefault.jpg)](https://www.youtube.com/watch?v=dZLcBbkZaes)

Detailed install video: https://youtu.be/dZLcBbkZaes

Note that this video was recorded before the integration existed so you can skip the blueprint and view install as those are now automatically provided for you.  Also note as of v 1.1.0 Chime TTS is no longer used and only Home Assistant `assist_satellite` devices types are supported.  Examples of those are View Assist Companion App and Home Assistant Voice Preview edition devices.

### Description

This custom sentence will sound an alert sound and broadcast an audio message to all View Assist satellites that are not in do not disturb mode. The text version of the message will appear on the screens of all View Assist satellites with displays that are not in hold mode.

## Usage

User says "Broadcast" plus the message to broadcast

# Requirements

- **View**: [Info view](../views/info)


## Changelog

| Version | Description                                                  |
| ------- | ------------------------------------------------------------ |
| v 1.1.0 | Work with VA integration; Only assist_satellite device types |
| v 1.0.3 | Rearrange variable order                                     |
| v 1.0.2 | Not using group                                              |
| v 1.0.1 | Change condition to match boolean not string                 |
| v 1.0.0 | Initial release                                              |
