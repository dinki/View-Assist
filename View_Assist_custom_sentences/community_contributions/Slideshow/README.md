# View Assist Slideshow & Gesture Controls

This package provides a clean, full-screen **Slideshow view** for View Assist, complete with interactive tap-to-pause controls, photo details overlay, quick menu button integration, and two reusable Home Assistant blueprints.

> [!NOTE]
> This view and its companion automations were specifically designed to work seamlessly with the [**Album Slideshow**](https://github.com/eyalgal/album_slideshow) custom integration (available via HACS). However, it is designed with flexibility in mind and can work with any other Home Assistant camera source or slideshow integration.

---

## Features

- 🖼️ **Fullscreen Photo View**: Displays active slideshow pictures using the satellite's background attribute with no obstructing elements.
- ⏯️ **Tap-to-Pause / Resume**: Single tap on the screen toggles pause/play on the slideshow.
- ⏸️ **Discreet Pause Badge**: When paused, a semi-transparent pause icon appears in the top-right corner.
- 📅 **Photo Details Overlay**: Swipe up or trigger to reveal a floating frosted-glass badge showing the photo capture date and location for a customizable duration.
- 👈 **Gesture Controls**: Configurable single-finger swipe gestures for entering the slideshow, advancing to next slide, returning home, and showing photo details.
- ⏱️ **Default View Timeout & Pause Suspension**: Utilizes View Assist's default view timeout when cycling; pausing the slideshow activates hold mode to keep the photo on screen indefinitely until unpaused.
- 🔄 **Background Sync**: Keeps satellite backgrounds in sync with the current image from any Album Slideshow camera.

---

## Files Included

1. `blueprint-slideshow_gesture_controls.yaml`: Automation blueprint for configurable swipe gestures and pause-aware view timeout.
2. `blueprint-sync_album_slideshow_background.yaml`: Automation blueprint for syncing Album Slideshow camera images to View Assist satellite backgrounds.
3. View definition: `View Assist dashboard and views/views/slideshow/slideshow.yaml`
4. Dashboard template: `slideshow` button card template in `dashboard.yaml`

---

## Prerequisites

- [View Assist](https://github.com/dinki/View-Assist) integration and dashboard.
- [Album Slideshow](https://github.com/eyalgal/album_slideshow) (recommended, available via HACS) or any camera entity providing photo streams.
- Touchscreen or gesture event entity (e.g. from openHASP, ESPHome, or Android touchscreen).

---

## Quick Setup

### 1. Register View in View Assist Dashboard
Add the slideshow view card into your View Assist dashboard (or let View Assist integration load it):
- Path: `slideshow`
- Card: `View Assist dashboard and views/views/slideshow/slideshow.yaml`

### 2. Add Slideshow to Menu Bar (Optional)
To add a quick-access Slideshow icon (`mdi:image-multiple`) to your satellite's menu bar, call the service:
```yaml
action: view_assist.add_status_item
data:
  entity_id: sensor.your_view_assist_device
  status_item: slideshow
  menu: true
```

### 3. Import Blueprints
- **Sync Album Slideshow Background**: Import `blueprint-sync_album_slideshow_background.yaml` and select your Album Slideshow camera and target View Assist devices.
- **Slideshow Gesture Controls**: Import `blueprint-slideshow_gesture_controls.yaml` and select your View Assist satellite sensor, gesture event entity, next slide button, and pause switch.
