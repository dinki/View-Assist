---
title: Slideshow View
---

The **Slideshow** view provides a full-screen image display designed for photo stream and album integrations. It features native View Assist hold/resume controls, an on-demand photo metadata badge, and quick menu bar integration.

:::info[Album Slideshow Compatibility]
This view and its associated automations were specifically designed to pair with the [**Album Slideshow**](https://github.com/eyalgal/album_slideshow) custom integration (available via HACS). However, it is also compatible with other Home Assistant camera source slideshows.
:::

---

## Features

- **Clean Fullscreen Presentation**: Displays the current image from the View Assist satellite's background attribute with no obstructing elements.
- **Native Hold / Resume**: Single tap on screen engages `mode: hold` to freeze the view indefinitely; double tap or tapping the native Hold icon returns to `mode: normal`.
- **Photo Metadata Overlay**: Swiping up (or setting `show_details: true`) shows an elegant frosted-glass overlay with the capture date and location.

---

## Prerequisites

- View Assist integration and dashboard.
- [Album Slideshow](https://github.com/eyalgal/album_slideshow) (recommended, available via HACS) or any camera entity providing image streams.

---

## Installation

Add the view to your View Assist dashboard (path: `slideshow`):
   - [Slideshow View Raw Code](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/slideshow/slideshow.yaml)

---

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
