---
title: Slideshow View
---

The **Slideshow** view provides a full-screen image display designed for photo stream and album integrations (such as Album Slideshow). It features interactive tap-to-pause/resume controls, an on-demand photo metadata badge, and quick menu bar integration.

---

## Features

- **Clean Fullscreen Presentation**: Displays the current image from the View Assist satellite's background attribute with no obstructing elements.
- **Tap-to-Pause / Resume**: Single tap on screen directly toggles pause/play on the photo stream.
- **Pause Badge Indicator**: When paused, a discreet pause icon (⏸) appears in the top-right corner.
- **Photo Metadata Overlay**: Swiping up (or setting `show_details: true`) shows an elegant frosted-glass overlay with the capture date and location.
- **Menu Bar Icon**: Includes a dashboard button-card template (`slideshow` / `mdi:image-multiple`) for instant navigation from the quick menu.

---

## Prerequisites

- View Assist integration and dashboard.
- An album slideshow source (such as the Album Slideshow integration or a camera entity providing image streams).

---

## Installation

1. Add the view to your View Assist dashboard (path: `slideshow`):
   - [Slideshow View Raw Code](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/slideshow/slideshow.yaml)
2. (Optional) Add the Slideshow icon to your View Assist device menu:
   ```yaml
   action: view_assist.add_status_item
   data:
     entity_id: sensor.your_view_assist_device
     status_item: slideshow
     menu: true
   ```

---

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
