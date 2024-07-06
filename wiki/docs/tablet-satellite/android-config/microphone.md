---
sidebar_position: 1
title: Microphone Streaming Software
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Installing Microphone Streaming Software
In order to leverage your tablet as a voice assistant satellite, you'll need to have an application installed that will be responsible for streaming the audio from your microphone on your local network. We'll leverage Stream Assist running on your Home Assistant instance to access those streams and pass the audio into the voice pipeline. We'll cover setting up Stream Assist in a future section.

The following Android applications have been tested and found to be working. The current recommendation is to use IP Webcam, however the choice is ultimately yours. You only need to install and configure ONE of the following applications.

- [IP Webcam](#ip-webcam)
- [RtpMic](#rtpmic)

---

## IP Webcam {#ip-webcam}
Detailed install video: https://youtu.be/-7cHfqZMa1c

### Installation
1. Download and install the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.pas.webcam).  

### Configuration
1. Find the IPWebcam Icon and tap it to launch.
1. Scroll down until you see the *IP Webcam settings* section.
1. Tap on **Power management** and under *Misc* Turn on **Disable notification** and **Stream on device boot**. 
1. Tap back to get back to the main setting screen.
1. Scroll down until you see the *Misc* section and tap on **Audio mode**. Choose **Audio Only**.

    :::info 
    While you can stream both audio and video via IPWebcam, we recommend using the **Audio Only** mode to reduce bandwidth and minimize video being streamed to your HA instance. Many users also prefer this due to the location of these tablet devices on the interior of their home such as in bedrooms.
    :::
2. Scroll down under the **Service Control** heading and tap on **Optional Permissions**.
1. Tap **Allow streaming in background** and accept Android system permissions when prompted.
1. Tap on **Show camera overlay**. This will prevent another window from appearing over your dashboard.
1. Tap back and then tap on **Start server**.  
1. When prompted, Allow all permissions as requested by Android OS (camera, microphone, etc.)

---

## RtpMic {#rtpmic}
:::note
RtpMic can only be installed via the Google Play store on devices running older versions of Android OS. Users have been successful manually sideloading the application on newer versions but that is beyond this tutorial.
:::
Detailed install video:
https://youtu.be/SkyErx7TE30

### Installation
1. Download and install the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.rtpmic&hl=en_US&gl=US)

### Configuration

1. Find the icon on your table and launch RtpMic.
1. Scroll down and start server.  Allow all permissions.
1. Enter the settings page and set:
    - You may want to increase gain if your mic detect is low on the meter.  I have set mine to 9 dB for the ThinkSmart device I am using
    - audio codec to G.711a
    - target addr to 255.255.255.255
    - target port to 55555
    - Auto start streaming 
    - Start at boot
1. Allow any permissions Android system may prompt for

