---
title: "Frequently Asked Questions"
sidebar_position: 8
---

# Frequently Asked Questions

<details>
  <summary>What is View Assist?</summary>

View Assist provides visual feedback for the Home Assistant Assist voice assistant using a collection of different automations, custom sentences, scripts, and extensions with the view being displayed on any Android device. Multiple devices can join the View Assist satellite network and interact. This is not limited to Android devices as voice only ESPHome satellites like the Home Assistant Voice Preview Edition are also supported. Some users have even brought Linux devices in as View Assist satellites as well.

</details>

<details>
  <summary>Why is the dashboard on my PC browser is showing a box telling me to register the device</summary>

You are trying to use View Assist on a PC or other nonView Assist satellite device. The dashboard is only for use on VA satellite devices. The dashboard is only used by View Assist satellites and will not work for general browsing outside of those registered devices.  The original intent of View Assist was to be an alternative to the Alexa Show and Next Home display devices.  Those are not general purpose tablets but a supplemental view for voice.  Further, the View Assist views provided are not static views like most Home Assistant views.  These views are dynamic.  The voice commands provide variable data stored in the attributes of each individual VA satellite device.  The views are set to look at those attributes.  This allows device independence and easy expansion of additional satellites without having to create multiple dashboards with a dedicated one per device.

All said, VA is a framework and you are more than welcome to adapt it to your needs but the way things are now will probably not change much, if any, unless someone can provide a suitable way of providing that underlying data with touch.

</details>

<details>
  <summary>Why am I'm seeing an error or no data when I manually browse to a view on the View Assist dashboard?</summary>

View Assist relies on Assist voice automations to provide information dynamically to the views. When you browse to views manually you will not have the underlying data the view needs to display something worth seeing.

</details>

<details>
  <summary>Why doesn't my view change when I issue the commands from the videos and wiki?</summary>

View Assist relies on automations from the View Assist blueprints to incorporate those controls. Some have made assumptions that everything is provide on View Assist integration install. This is incorrect. The View Assist controls are ala carte in that you can choose which you want to incoroporate and which you do not. Additionally, the blueprints allow for more control of what sentence triggers to use, what language to communicate in and other options that cannot be set globally for all users.

See the sidebar menu option ['Automations and Views'](./extend-functionality/index.md) for more information.

</details>
