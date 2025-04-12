# Sound Machine

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2FSound_Machine%2Fblueprint-soundmachine.yaml)

This blueprint enables the user to play ambient sounds for relaxation or noise cancelation

## Requirements and installation

* Install blueprint using button above and configure options
* Install the [play sound on media player](https://github.com/dinki/View-Assist/tree/main/View_Assist_scripts/Play_Sound_on_Media_Player) script.  Open the blueprint and click 'save script' button at bottom.  Keep all options the same and click 'rename' to make the script available for use
* Install the [play sound on media player repeat](https://github.com/dinki/View-Assist/tree/main/View_Assist_scripts/Play_Sound_on_Media_Player_Repeat) script.  Open the blueprint and click 'save script' button at bottom.  Keep all options the same and click 'rename' to make the script available for use
* Find and upload ambient sound files to play when the timer expires.  Need help?  See the Stream Assist video where we discuss how to find these and where to upload
 
Optional
* If you would like to use timed play (play thunder sound machine for 5 minutes) download and install the [viewassist-timer.py](https://github.com/dinki/View-Assist/blob/main/View_Assist_custom_sentences/Alarms_Reminders_Timers/viewassist-timer.py) pyscript file (.py) Need help?  See the pyscript video

Configure the dictionary of sounds in the blueprint.  Examples have been given.  You must follow the same format for the automation to work

## Usage

Use your wakeword and say things like:

* Start the rain sound machine
* Play the thunder sound machine for thirty minutes
* Stop the sound machine

It is important to stop the sound machine.  The script will continue to run in the background which could lead to not being able to start the sound machine again in the future until the stop command is given or Home Assistant is restarted

