
# View Assist Control Automations

The View Assist display satellites have different modes for how screens are shown on the device and for how long. This behavior is controlled by an automation. Each View Assist visual device will need its own control automation.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_control_automations%2Fblueprint-devicecontrol.yaml)

<a href="https://www.youtube.com/watch?v=Vrm4TCotEqA"><img src="https://img.youtube.com/vi/Vrm4TCotEqA/mqdefault.jpg" width="60%"></a>

Detailed install video:
https://youtu.be/Vrm4TCotEqA

Additional functionality has been added since the video was posted.  

* Added ability to give visual feedback when user uses Home Assistant built in intents like 'Turn on the living room lights' or 'Open the garage door'.  View Assist will now open a view and show the entity being changed.  Users will need to install the [intent view](https://github.com/dinki/View-Assist/tree/main/View%20Assist%20dashboard%20and%20views/views/intent)

# Change Log
v 1.0.0 Initial release

v 1.2.0 Add intent view for built in Home Assistant sentences

v 1.2.1 Provide additional visual feedback for devices changed using HA built in sentences (thanks @JimmyJamesBob!)
