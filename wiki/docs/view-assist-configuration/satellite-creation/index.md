---
title: "View Assist Satellite Creation"
sidebar_position: 1
---

# Satellite Device Creation

Despite the name, View Assist supports both devices with and without displays.  These devices can use the same custom sentences and can interact with each other.  These are the instructions for adding these devices:

In Home Assistant go to Settings -> Devices and Services -> Add integration -> Search for View Assist and click 'Add'

![](./vacreate1.png)

Choose the type of satellite device you are wanting to create and click 'Next'

![](./vacreate2.png)

Here we are configuring a device with display.  Note that the audio only devices will not have the 'Display Device' or the 'Mimic for view development' options but everything else is the same.  We will need to fill out these core configuration options before the device can be used.  Here's the explanation of the fields:

    - **Satellite Name:** The satellite device name (eg ViewAssist-livingroom)
    - **Microphone Device:**  Used to assign microphone to View Assist device.  See the microphone section for set up instructions
    - **Media Player Device:** Used to assign the media player used for View Assist audio message playback
    - **Music Player Device:** Used to assign the media player used for View Assist music playback.  This can be the same as Media Player Device or different
    - **Display Device:** Used to assign display device to View Assist device.  See the display section for set up instructions
    - **Mimic for view development:** This is an advanced option for those who want to develop views on a PC.  Default value is off

After setting these values you can then click 'Submit' and the View Assist satellite will be ready for use!  Note that the View Assist dashboard will be automatically created after you create your first satellite with a display device.
