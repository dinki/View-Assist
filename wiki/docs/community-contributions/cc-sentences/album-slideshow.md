---
title: Album Slideshow & Gesture Controls
---

This contribution provides two blueprints for integrating album slideshows with View Assist:
1. **Slideshow Gesture Controls**: Configurable single-finger swipe gestures for switching into the Slideshow view, cycling to the next photo, returning to the Home/Clock view, and displaying photo capture metadata badges. Pausing the slideshow activates hold mode to keep the photo displayed until unpaused.
2. **Sync Album Slideshow Background**: Automatically synchronizes the View Assist satellite's background attribute whenever an Album Slideshow camera changes images.

:::info[Album Slideshow Compatibility]
These blueprints and the companion Slideshow view were designed to work with the [**Album Slideshow**](https://github.com/eyalgal/album_slideshow) custom integration (available via HACS). However, they are compatible with other Home Assistant camera sources and slideshow integrations.
:::

---

## Blueprints Included

### 1. Slideshow Gesture Controls

[![Import Slideshow Gesture Controls to Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FSlideshow%2Fblueprint-slideshow_gesture_controls.yaml)

- **Blueprint Raw File**: [blueprint-slideshow_gesture_controls.yaml](https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/Slideshow/blueprint-slideshow_gesture_controls.yaml)
- **Features**:
  - **Clock ➔ Slideshow**: Swipe left (`left_1`) from the clock screen opens the Slideshow using the satellite's default view timeout.
  - **Next Slide**: Swipe left (`left_1`) while on the Slideshow advances to the next photo.
  - **Return Home**: Swipe right (`right_1`) exits to the Home screen.
  - **Photo Metadata**: Swipe up (`up_1`) displays the photo date and location badge for a configurable duration.
  - **Pause-Aware Timeout**: Relies on the default View Assist view timeout during active cycling; pausing the slideshow engages hold mode to suspend timeout until resumed.

---

### 2. Sync Album Slideshow Background

[![Import Sync Album Slideshow Background to Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FSlideshow%2Fblueprint-sync_album_slideshow_background.yaml)

- **Blueprint Raw File**: [blueprint-sync_album_slideshow_background.yaml](https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/Slideshow/blueprint-sync_album_slideshow_background.yaml)
- **Features**:
  - Updates target View Assist device background attributes on every photo transition from an Album Slideshow camera.

---

## Prerequisites

- [View Assist](https://github.com/dinki/View-Assist) integration and dashboard.
- [Album Slideshow](https://github.com/eyalgal/album_slideshow) (recommended, available via HACS) or compatible image stream integration.
- Touchscreen / gesture event entity (e.g. VACA, openHASP, ESPHome, or Android touchscreen).

---

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
