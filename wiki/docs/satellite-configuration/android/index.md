---
title: Android Configuration
sidebar_position: 2
---

# Configuring Your Android Tablet

An Android device is the most common example of a View Assist Satellite. The various components outline through this guide have been tested on several different Android tablets running several various versions of the Android operating system. The initial device used for the proof of concept was a 2016 Amazon Fire 7HD tablet running Android 5. It's because of this we are confident to say that this method should work on any device that is that old or newer. Wake Word detection is done on your Home Assistant instance as audio is constantly being streamed from your tablet to your HA server.

![](androidworkflow.png)

## Prerequisites
1. Android device running Android 5 or newer
1. Know the IP Address of your tablet

    :::info[Note]
    While beyond the scope of this guide, we highly recommend you setup your tablet with a fixed IP address as several parts of the configuration require you knowing the IP address of your tablet. If the IP address were to change, it would break portions of
    your configuration going forward.
    :::