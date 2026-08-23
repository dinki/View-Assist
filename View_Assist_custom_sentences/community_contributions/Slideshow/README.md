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

## Blueprints Included

### 1. Slideshow Gesture Controls
[![Import Slideshow Gesture Controls to Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FSlideshow%2Fblueprint-slideshow_gesture_controls.yaml)

- Automation blueprint for configurable swipe gestures and pause-aware view timeout.

### 2. Sync Album Slideshow Background
[![Import Sync Album Slideshow Background to Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FSlideshow%2Fblueprint-sync_album_slideshow_background.yaml)

- Automation blueprint for syncing Album Slideshow camera images to View Assist satellite backgrounds.

---

## Prerequisites

- [View Assist](https://github.com/dinki/View-Assist) integration and dashboard.
- [Album Slideshow](https://github.com/eyalgal/album_slideshow) (recommended, available via HACS) or any camera entity providing photo streams.
- Touchscreen or gesture event entity (e.g. VACA, openHASP, ESPHome, or Android touchscreen).

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
Click either of the **Import to Home Assistant** badges above, or import manually from the repository paths.
