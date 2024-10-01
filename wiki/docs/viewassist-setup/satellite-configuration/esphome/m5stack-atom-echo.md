---
title: M5Stack Atom Echo
sidebar_position: 1
---

![Image](../../../supported-devices/esphome-devices/m5stackecho.jpg)

The M5Stack Atom Echo Smart Speaker ([Amazon](https://amzn.to/4eC8Tto)/[M5Stack Shop](https://shop.m5stack.com/collections/m5-controllers/products/atom-echo-smart-speaker-dev-kit)/[AliExpress](https://www.aliexpress.us/item/3256803113017446.html?aff_platform=portals-tool&sk=_A8G2YF&aff_trace_key=90326d2a90444b4887632f62dd533ce4-1654058373639-07963-_A8G2YF&terminal_id=c5517a8c9bb44b4fb32147398fbc2576&aff_fcid=90326d2a90444b4887632f62dd533ce4-1654058373639-07963-_A8G2YF&tt=CPS_NORMAL&aff_fsk=_A8G2YF&gatewayAdapt=glo2usa4itemAdapt)) is a small device that allows for easy set up via a webbased flashing tool.  This is one of the easiest devices to get started with Home Assistant voice.  

## Installation

Installation of the firmware can be handled via the web flashing tool found at:

https://esphome.io/projects/index.html

Simply select 'Voice assistant' click the M5Stack option and click connect.

Then after follow the tutorial found here:

https://www.home-assistant.io/voice_control/thirteen-usd-voice-remote/

You will then fast forward through most of the configuration steps.  Note that you will not need to set up a timer helper for this device as that is only used for View Assist satellites with displays.

Follow this link to add your M5Stack Atom Echo device as a voice only satellite in View Assist:

https://dinki.github.io/View-Assist/docs/viewassist-setup/homeassistant-configuration/viewassist-configuration/device-configuration#satellite-custom-device-configuration

### Use the M5Stack Atom Echo as a microphone only (Optional)

User @Tohur has come up with a clever way to use an M5Stack Atom Echo device as a microphone replacement for his inferior microphone on their Android tablet.  This use case is not common and most can skip this altogether but for some it may prove to be very useful.

@Tohur explains how to use his method here:

