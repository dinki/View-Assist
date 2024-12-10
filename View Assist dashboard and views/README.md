# View Assist Dashboard 2.0

We have been hard at work making the frontend of View Assist look better.  It was a team effort and I would like to thank JimmyJamesBob and Flab for their hardwork in making this possible.  It was quite a lot of work and the results are fantastic.  View Assist is now looking like it should.  Below you will find some of the improvements as well as how to update.  We welcome your feedback, observations and suggestions.

## Notable improvements
* The new blueprint offloads some of the work previously done by hardcoded values in the dashboard and/or views.  Things like the View Assist group, weather entity, and 24 hour clock preference are now handled within.  This will allow for more customization per VA satellite
* Visually the user now has the option to set a different default background image per device.  The user can also optionally set a timed interval in EITHER minutes or hours to rotate the image (requires [Pyscript script script](https://github.com/dinki/View-Assist/blob/main/View_Assist_control_automations/viewassist-select_random_image.py)
* A new Assist prompt called 'blur pop up' is now the default.  This popup happens when you say the wake word.  The old Assist bar is still available for those who would like to continue using it
* Many of the values that were required in the VA device config are now customizable from the blueprint.  These include mode, view timeout, do not disturb and others.  They can be removed from the VA device config when you like.  This is not a breaking change.  See the new minimum standard VA device config [here](https://github.com/dinki/View-Assist/blob/main/View%20Assist%20device%20configuration/device_config_example.yaml)
* Icon size and font style are now selectable through the blueprint.  This will allow for even more customization
* We are introducing 'launch icons' which will act as shortcut buttons to your cutom tasks.  This can be to switch to camera views, turn on/off lights, etc.  These are tied to action calls and can be added as a persistent icon for these functions
* Changes in CSS now allow for better placement of elements and better use of space.  The shifting of elements when icons appear/disappear has finally been resolved!
* User now has an option to use either Stream Assist, HassMic, or Home Assistant Voice Assistant inputs.  We will be adding other types in the future
* Dates are now localized for our international users

## Instructions for installing the new dashboard for existing users:

* Back up your existing dashboard!  This is 100% not optional.
  * Go to your View Assist dashboard then click the pencil icon in the top right corner, then the three dots, then `Raw configuration editor`, then copy paste the entire contents into a text file and save this on your computer for safe keeping
* Consider making a backup through Home Assistant as another just in case.  You should do this.
* Copy the new dashboard code from [here](https://github.com/dinki/View-Assist/blob/main/View%20Assist%20dashboard%20and%20views/dashboard/dashboard.yaml) onto your clipboard
* Go back to your dashboard editor from the step where you made the backup copy and CAREFULLY paste over the code from the beginning down to the last line before `views:` .  You are attempting to replace what exists above that line only.  Hit save
* You'll need to update the code for the following views to take advantage of the new functions if you are.  You only need to update views you are currently using or plan to use.  You can find these views [here](https://github.com/dinki/View-Assist/tree/main/View%20Assist%20dashboard%20and%20views/views)
  *  Clock
  *  Music
  *  Webpage
  *  Camera
* Install the updated blueprint.  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_control_automations%2Fblueprint-devicecontrol.yaml)
* Use the above blueprint to configure/reconfigure your VA devices


!!!IMPORTANT!!!  Any changes to the blueprint will REQUIRE a restart of Home Assistant to take effect
