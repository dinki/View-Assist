---
sidebar_position: 1
---

# Welcome to View Assist

View Assist provides visual feedback for the Home Assistant Assist voice assistant using a collection of different automations, custom sentences, scripts, and extensions with the view being displayed on any Android device.  Multiple devices can join the View Assist satellite network and interact.  This is not limited to Android devices as voice only ESPHome satellites like the Home Assistant Voice Preview Edition are also supported.  Some users have even brought Linux devices in as View Assist satellites as well.   


[![](https://img.youtube.com/vi/t0jG4LZzKqs/mqdefault.jpg)](https://www.youtube.com/watch?v=t0jG4LZzKqs)

Demo Video:  https://www.youtube.com/watch?v=t0jG4LZzKqs


This project is designed so that you can pick and choose the parts that you want for your needs.  The custom sentences are written to accomodate those who may only be interested in voice only.  The dashboard views may be interesting to others who are writing their own custom sentences.

## How Does View Assist Work?

View Assist works by creating custom satellite entities using the View Assist integration.  This integration handles things like identifying the input and output devices attached, different modes, screen timeouts, browser control and many more functions.  The custom views are written in a way that they are aware of the device that is displaying the view and can produce different output on different devices at the same time.  The View Assist satellite devices are also capable of communicating with each other which allows for creating broadcast announcements to selected devices.

View Assist is easily customizable.  Custom sentences are provided as blueprints which makes configuration easy.  Users are able to choose which blueprints to use so they can select only the functions that interest them.  This method has proven to extend the Home Assistant voice experience beyond what is provided by default.  It is also provides an easy way for users to share their creations with others.

## What do I need to get started?

While View Assist did start as a project for Android tablets, it has been extended to work with Home Assistant Voice Preview Edition and ESPHome voice only satellites as well.  In addition, other users have reported sucess using Android phones and Linux devices as well.  The only real requirements for using View Assist with a display device is a means to run a web browser and a means to have the device microphone output streamed back to Home Assistant.  On this site you will find detailed instructions for Android and ESPHome devices but we will add other devices as they are reported by the community.
