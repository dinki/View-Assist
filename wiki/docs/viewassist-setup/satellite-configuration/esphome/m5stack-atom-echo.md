---
title: M5Stack Atom Echo
sidebar_position: 1
---

![Image](../../../supported-devices/esphome-devices/m5stackecho.jpg)

The M5Stack Atom Echo Smart Speaker ([Amazon](https://amzn.to/4eC8Tto)/[M5Stack Shop](https://shop.m5stack.com/collections/m5-controllers/products/atom-echo-smart-speaker-dev-kit)/[AliExpress](https://www.aliexpress.us/item/3256803113017446.html?aff_platform=portals-tool&sk=_A8G2YF&aff_trace_key=90326d2a90444b4887632f62dd533ce4-1654058373639-07963-_A8G2YF&terminal_id=c5517a8c9bb44b4fb32147398fbc2576&aff_fcid=90326d2a90444b4887632f62dd533ce4-1654058373639-07963-_A8G2YF&tt=CPS_NORMAL&aff_fsk=_A8G2YF&gatewayAdapt=glo2usa4itemAdapt)) is a small device that allows for easy set up via a webbased flashing tool.  This is one of the easiest devices to get started with Home Assistant voice.  

## Installation

if your M5Stack Atom Echo is a recently ordered device it most likely has out of the box firmware ready to go and is as easy as doing the inital setup via Settings -> Devices & services over bluetooth on your Home Assistant instance to setup your wifi and aquire your api encryption key, making sure to copy the key for safe keeping.

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

Tohur here, this setup will require you to have already done the Andriod setup here https://dinki.github.io/View-Assist/docs/viewassist-setup/satellite-configuration/android skipping/ignoring any Stream Assist setup unless you require it for other View Assist satellites.

Initially follow the setup above for your M5Stack Atom echo.

**ESPHome**

Next we install ESPHome by going to Settings -> Add-ons and clicking the button on the bottom right and searching for ESPHome or   

[![ESPHome](https://my.home-assistant.io/badges/supervisor_addon.svg 'ESPHome')](https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon)

Make sure to  turn on the sidebar view for easy access to ESPHome. Once you have ESPHome installed and running go to the ESPHome webui in a Chromium based browser and you should see your configured M5Stack Atom Echo ready to be adopted by ESPHome. Follow the adoption process and once its configured click edit and paste the provided firmware yaml. 

The firmware yaml can be found here: [m5stack-atom-echo.yaml](./m5stack-atom-echo.yaml)

Take note of the follow in the new config:

```
substitutions:
  name: "m5stack-atom-echo"
  friendlyname: "M5Stack Atom Echo"
  api_key: "encryption key"
  HA_mediaplayer: "media_player.bedroom"
```

Replace name and friendlyname values with your device name and friendlyname and replace the api_key value with your encryption key aquired earlier. HA_mediaplayer should be the media player entitiy for your View Assist Android satellite as with the firmware you are only using the microphone of the M5Stack Atom echo and all audio is outputted over your View Assist Android satellite. Also make sure to  look the the cofig  in the wfi section and make sure you have an static ip set matching your network details.

Once you have your config edited make sure to save before clicking Install. If wifi is already setup and ready to go you should be able to install using the wifi option other wise choose to install from the browser you are using and by plugging the Atom Echo directly into your HA Instances machine and install directly over USB.



Once Install is complete and your Atom echo is booted go to Settings -> Devices  & Services -> Entities and search for your devices entities and take note of the entitiy ids of the newly added STT sensor and MIC switch. The STT sensor will be your mic_device in your configuration.yaml from the View Assist setup and the MIC switch will be used as the mic device in the device control automation. From here after adding  your Atom echo to your already setup Android satellite replacing the the mic_device with the Atom  Echos SST sensor reboot your Home Assistant.



Thank you and If you need any help I am in discord any contributions to this are welcomes as  the only thing not working is the intent view as we need to create a intent matching system and sensor for View Assist (there is already a place holder intent sensor).
