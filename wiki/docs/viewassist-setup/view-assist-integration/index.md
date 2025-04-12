---
sidebar_position: 5
title: "Step Four: View Assist Integration"
---

Welcome to the long awaited, much anticipated View Assist integration beta!  Some of the notable improvements include:

* All configuration done within the integration.  The days of editing YAML files are over!
* The View Assist dashboard is now autocreated when a View Assist device with visual output is configured.  This includes assets like default images and soundfiles to be downloaded and preconfigured for use
* A new view_assist directory will be created in your config directory to hold VA dashboard and views along with an easy storage location for your images and sound files to use with View Assist
* Views can now be updated through an action call
* Users can create their own views as before and use a save view action that will store a local copy that will then be used when an autoregeneration of the dashboard action is called
* Timers and alarms survive restarts!
* The external python set_state.py and control blueprint per device are no longer needed
* Some external pyscripts have now been integrated simplifying the install process
* Full support for both BrowserMod and the new [Remote Assist Display](https://github.com/michelle-avery/remote-assist-display) has been added
* Many quality of life improvements have been added on both the user and developer facing sides

A HUGE thank you goes out to Mark Parker @msp1974 for his MASSIVE help with making this a reality.  Mark has written the majority of the integration with my guidance.  You should check out his [Home Assistant Integration Examples](https://github.com/msp1974/HAIntegrationExamples) Github if you are intestered in creating your own integration.  His work has propelled View Assist to first class in very short order.  We would not be where we are today without his continued efforts and the hours and hours he has put in to make View Assist better!  Thanks again Mark!



# Installing the View Assist Integration

## Notes for existing VA users

**A BIG warning for folks who will be updating.  This is a major rewrite so you will be starting from scratch for the most part.  You will definitely want to do a backup of your current VA settings and views and possibly save a copy of your current dashboard to avoid from losing something you would like to keep!**

You will want to delete your View Assist dashboard before installing.  I suggest that you save your dashboard as a text file (Raw configuration copy/paste).  You will need to UPDATE your View Assist blueprints using the new blueprints.  This is done by importing the new version of the blueprint and choosing to update the existing.  This SHOULD allow for you to keep all settings but be warned that this is beta so problems may exist with keeping these settings in some cases.


## HACS
* Install HACS if you have not already
* Open HACS and click three dots in right corner -> Custom Repositories -> then paste `https://github.com/dinki/view_assist_integration/` in 'Repository' and choose type 'Integration' then click 'Add'
* Now search for 'View Assist' in HACS
* Click "Add" to confirm, and then click "Download" to download and install the integration
Restart Home Assistant
* Search for "View Assist" in HACS and install then restart
* In Home Assistant go to Settings -> Devices and Services -> Add integration -> Search for View Assist and add
* Configure the device(s)

## Manual Install

This integration can be installed by downloading the [view_assist](https://github.com/dinki/view_assist_integration/tree/main/custom_components) directory into your Home Assistant /config/custom_components directory and then restart Home Assistant.  We have plans to make this easier through HACS but are waiting for acceptance.
