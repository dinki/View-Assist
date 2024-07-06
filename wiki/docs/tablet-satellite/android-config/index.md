---
title: Android Configuration
sidebar_position: 2
---

# Configuring Your Android Tablet

An Android device is used for the display, voice input, and audio output. The device used for the POC is a 2016 Amazon Fire 7HD tablet running Android 5. It's because of this I am confident to say that this method should work on any device that is that old or newer. Wake Word detection is done on your Home Assistant instance as audio is constantly being streamed from your tablet to your HA server.

## Prerequisites
1. Android device running Android 5 or newer
1. Know the IP Address of your tablet

    :::info
    While beyond the scope of this guide, we highly recommend you setup your tablet with a fixed IP address as several parts of the configuration 