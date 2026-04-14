# Play Radio with Music Assistant

Play radio stations with View Assist using Music Assistant.

This blueprint supports both:

- **Legacy commands** using a fixed station ID --> This means that every radio station needs its own automation.
- **Alias-based commands** using `{station_name}` --> With aliases, one automation is sufficient

The updated logic is designed to stay compatible with older automations while making new setups much easier to configure.

### It is recommended to use the new version with aliases for new automations


## Requirements

- Music Assistant server installed and integrated with Home Assistant
- Create a free account on Tune In and add some stations to your favorites on the Tune In website
- Install TuneIn Radio music provider in Music Assistant, configure, and allow time to sync
- View: [Music view](../views/music)
- The TuneIn station ID as seen in Music Assistant (see instructions for finding below)
- The recently added musicplayer_device must be added to your View Assistant device configuration as explained in the [Satellite Custom Device Configuration](https://github.com/dinki/View-Assist/wiki/View-Assist-device-configuration#satellite-custom-device-configuration) portion of the wiki. This should be a Music Assistant player device. Typically these will be named the same as your mediaplayer_device but with a \_2 on the end
- The `musicplayer_device` added to your View Assist device configuration as described in the wiki
- At least one radio station available in Music Assistant

## What changed in v1.3.0

- Added support for **alias-based station matching**
- Kept compatibility with the original fixed-station setup
- Simplified the internal logic
- Removed the extra mode handling
- Prevents playing the wrong fallback station when using alias-based radio commands
- Added a more user-friendly UI for entering station aliases

## How it works

The blueprint now decides automatically which path to use:

### Legacy path

If your command does **not** contain `{station_name}`, the blueprint uses the configured fixed station ID. 

This keeps older automations working as before.

### Alias path

If your command **does** contain `{station_name}`, the blueprint will:

1. Read the spoken station name
2. Try to match it against the configured alias list
3. Play the matching station if found
4. Stop immediately if no alias matches

This avoids accidentally playing the wrong station.

## Installation

### 1. Create an automation

Go to:

`Settings -> Automations & Scenes -> Automations`

Then:

1. Create a new automation
2. Choose **Use Blueprint**
3. Select **Play Radio with Music Assistant**

## Configuration

### Language

Select the language used for responses.

### Command

This is the sentence pattern View Assist will listen for.

You can continue using a legacy fixed command, or switch to the new alias-based format.

#### Legacy example

- en: `play Big 102.1`
- de: `Spiele Big 102.1`

#### Alias-based example

- en: `(start | play | listen) [to] radio [station] {station_name}`
- de: `[den] (starte | spiele) radio [sender] {station_name} [hören]`

If you want to use aliases, your command must include `{station_name}`.

<img width="1054" height="115" alt="Screenshot 2026-04-13 171658" src="https://github.com/user-attachments/assets/639cda2c-5e1c-4d3e-8cdb-f35f62c0e706" />

### Station

This is the fixed Music Assistant station ID used by the legacy path.

It is only used when your command does **not** contain `{station_name}`.

<img width="1092" height="821" alt="Screenshot 2026-04-13 172056" src="https://github.com/user-attachments/assets/3cadeb6c-e973-4a93-8c69-3a67ac7bb65b" />

### Station aliases

This is the new alias-based configuration.

Each entry lets you define:

- a spoken alias
- the real Music Assistant station ID
- an optional display/station name for voice output

<img width="542" height="410" alt="Screenshot 2026-04-13 172303" src="https://github.com/user-attachments/assets/6c15d862-bdc6-41d8-83f4-ee9cef40a3d6" />
<img width="542" height="410" alt="Screenshot 2026-04-13 172158" src="https://github.com/user-attachments/assets/45782513-2f1c-4094-83ba-8f9f5244d7a2" />

## How to find the station ID

Open Music Assistant and go to the radio section.

Find the station you want to use and copy the station ID exactly as shown in Music Assistant.

![image](https://github.com/user-attachments/assets/026e51e3-bd5c-440f-ba0e-e221a40e9f9a)


## Notes

- Existing automations should continue to work as long as they keep using the original fixed-station style command
- To use the new alias-based behavior, update the command so it includes `{station_name}`
- Alias-based commands are safer because they prevent the wrong default station from being played
- The alias UI is easier to configure than raw YAML lists or dictionaries

## Changelog

| Version | Description |
|--------:|-------------|
| 1.3.0 | Added alias-based station matching, improved UI configuration, simplified logic, preserved legacy compatibility |
| 1.2.1 | Add translations |
| 1.2.0 | Various improvements |
| 1.1.0 | Various improvements |
| 1.0.3 | Bug fix plus add ability to have custom announcement |
| 1.0.2 | Update to use conditional response |
| 1.0.1 | Update to use `music_assistant` action |
| 1.0.0 | Initial release |
