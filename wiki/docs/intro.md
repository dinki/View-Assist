---
sidebar_position: 1
---

# Welcome to View Assist

View Assist provides visual feedback for the Home Assistant Assist voice assistant using a collection of different automations, custom sentences, scripts, and extensions with the view being displayed on any Android device.  Multiple devices can join the View Assist satellite network and interact.  This is not limited to Android devices as ESPHome satellites are also supported.  The project is still a work in progress but is fully functional.  


[![](https://img.youtube.com/vi/t0jG4LZzKqs/mqdefault.jpg)](https://www.youtube.com/watch?v=t0jG4LZzKqs)

Demo Video:  https://www.youtube.com/watch?v=t0jG4LZzKqs


This project is designed so that you can pick and choose the parts that you want for your needs.  The custom sentences can be modified for those who may only be interested in voice only.  The dashboard views may be interesting to others who are writing their own custom sentences.

## How Does View Assist Work?

View Assist works by creating custom satellite entities via Home Assistant configuration and adding these satellites to a Home Assistant group.  A control automation is created per satellite device which handles things like identifying the input and output devices attached, different modes, screen timeouts and some of the core functions.  The custom views are written in a way that they are aware of the device that is displaying the view and can produce different output on different devices at the same time.  The View Assist satellite devices are also capable of communicating with each other which allows for creating broadcast announcements to selected devices.

View Assist is easily customizable once the base configuration is in place.  Custom sentences are provided as blueprints which makes configuration easy.  Users are able to choose which blueprints to use so they can select only the functions that interest them.  This method has proven to extend the Home Assistant voice experience beyond what is provided by default.  It is also provides an easy way for users to share their blueprints with others.

## What do I need to get started?

While View Assist did start as a project for Android tablets, it has been extended to work with ESPHome voice only satellites as well.  In addition, other users have reported sucess using Android phones as well.  The only real requirements for using View Assist with a display device is a means to run a web browser and a means to have the device microphone output streamed back to Home Assistant.  On this site you will find detailed instructions for Android and ESPHome devices but we will add other devices as they are reported by the community.
