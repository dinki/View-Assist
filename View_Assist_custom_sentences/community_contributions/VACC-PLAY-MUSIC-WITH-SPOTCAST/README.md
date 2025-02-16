# View Assist - Play Music with Spotcast

This project provides a pair of Home Assistant blueprints that use the [SpotcastV5](https://github.com/fondberg/spotcast/tree/dev) and [ViewAssist](https://github.com/dinki/view_assist_integration) integrations to control Spotify music playback with natural language commands and expose it to LLMs as a tool with a script.

The blueprints include:

- **Automation Blueprint:**  
  Enables music playback in multiple modes:
  - **Play DJ (Recently Played):** Plays your recently played songs.
  - **Play Search (Music Search):** Plays music based on search keywords (e.g., album, artist, playlist, or track name).
  - **Transfer Playback:** Allows you to move the active playback from one area to another. When a specific area is provided, the music plays on that media player, and the corresponding display (satellite) updates accordingly.

- **Script Blueprint:**  
  Creates a script that constructs and sends a natural language command to the Home Assistant conversation agent via the `conversation.process` service. This script dynamically builds the voice command based on the following parameters:
  - `music_type`: Defines the type of request—`recent`, `search`, or `transfer`.
  - `music_query`: The query used when searching for a specific song, artist, or genre (required for search requests).
  - `area`: The target area where the music should play or be transferred.

---

## Features

- **No premium Spotify account needed**  
  Works with both premium and non-premium Spotify accounts.

- **Playback Modes:**
  - **DJ Mode:**  
    Plays music using the context of your recently played songs.
  - **Search Mode:**  
    Plays music based on search keywords provided by the user.
  - **Transfer Mode:**  
    Moves the current playback to a specified area/media player.

- **Zone-Based Control:**  
  When an area is specified (using the `{area}` variable), the automation directs playback to the media player named in the format `media_player.<area>_speaker`. If no area is provided, it defaults to the last active media player or default one on the associated satellite.

- **LLM Integration:**  
  The script blueprint exposes the functionality to language model integrations (LLMs) or Home Assistant's built-in conversation agent. **Important:** Do not modify or remove the default English trigger phrases in the automation blueprint. Additional phrases can be added following the same structure.

---

## Prerequisites

- **Home Assistant:**  
  Ensure you are running `min_version: "2024.10.0"` of Home Assistant.

- **Integrations:**
  - [SpotcastV5](https://github.com/fondberg/spotcast/tree/dev)
  - [ViewAssist](https://github.com/dinki/view_assist_integration)
  - [ViewAssist- Music view](https://github.com/dinki/View-Assist/blob/main/View%20Assist%20dashboard%20and%20views/views/music/music.yaml)

- **Entity Naming Convention:**  
  Your media player entity IDs must follow the format:  
  `media_player.<area>_speaker`  
  where `<area>` corresponds to the room or zone where the speaker is located.

---

## Installation

### 1. Automation Blueprint

#### Method A: Auto-Installation Button

Click the button below to open Home Assistant and import the automation blueprint directly:

[![Open in Home Assistant](https://my.home-assistant.io/images/open-in-ha-blue.svg)](https://my.home-assistant.io/redirect/blueprint/?url=https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/VACC-PLAY-MUSIC-WITH-SPOTCAST/blueprint-playmusicwithspotcast-automation.yaml)

#### Method B: Manual Installation

1. Download the file [`blueprint-playmusicwithspotcast-automation.yaml`](https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/VACC-PLAY-MUSIC-WITH-SPOTCAST/blueprint-playmusicwithspotcast-automation.yaml).
2. Place it in the following directory on your Home Assistant configuration: `/config/blueprints/automation/relu/blueprint-vacc-playmusicwithspotcast-automation.yaml`
3. In Home Assistant, create a new automation from blueprint and fill in the required inputs:
- **Group Entity:** The group containing your ViewAssist satellites (e.g., `group.viewassist_satellites`).
- **Dashboard Info View:** The path to your ViewAssist dashboard (e.g., `/dashboard-viewassist/music`).
- **Display Navigation App:** The service used for navigating the display (e.g., `remote_assist_display.navigate`).

---

### 2. Script Blueprint

#### Method A: Auto-Installation Button

Click the button below to open Home Assistant and import the script blueprint directly:

[![Open in Home Assistant](https://my.home-assistant.io/images/open-in-ha-blue.svg)](https://my.home-assistant.io/redirect/blueprint/?url=https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/VACC-PLAY-MUSIC-WITH-SPOTCAST/blueprint-vacc-playmusicwithspotcast%20-%20LLMscript.yaml)

#### Method B: Manual Installation

1. Download the file [`blueprint-vacc-playmusicwithspotcast - LLMscript.yaml`](https://raw.githubusercontent.com/dinki/View-Assist/main/View_Assist_custom_sentences/community_contributions/VACC-PLAY-MUSIC-WITH-SPOTCAST/blueprint-vacc-playmusicwithspotcast%20-%20LLMscript.yaml).
2. Place it in the following directory on your Home Assistant configuration: `/config/blueprints/script/relu/blueprint-vacc-playmusicwithspotcast-LLMscript.yaml`

**Note:** Verify that the file name does not contain any unwanted spaces or special characters.

3. After installation, ensure the script is exposed to the Home Assistant conversation agent so it can be triggered via voice commands.

---

## How to Use

1. **Voice Commands & Triggers:**  
The automation blueprint comes with a set of default trigger phrases:
- **Play DJ Mode:**  
  Examples:  
  - "I want to play my recent music"  
  - "I want to play my recent songs on {area} speaker"
- **Play Search Mode:**  
  Examples:  
  - "play {music}"  
  - "play {music} on {area} speaker"
- **Transfer Music:**  
  Examples:  
  - "move the music on {area} speaker"  
  - "transfer the music on {area} speaker"

**Important:** Do not modify or remove the default trigger phrases if you plan to use the LLM integration. Additional phrases in another languages can be added following the same structure.

2. **Action Flow:**  
Depending on the command received, the blueprint will:
- Call the appropriate Spotcast service (`spotcast.play_dj`, `spotcast.play_from_search`, or `spotcast.transfer_playback`).
- Update the corresponding ViewAssist satellite display to reflect the active media player.
- Set the state of the satellite device to indicate that music is playing.

3. **Script Execution:**  
The script blueprint constructs a command string based on the provided inputs (`music_type`, `music_query`, and `area`) and sends it via the `conversation.process` service. This allows for natural language interaction with your Home Assistant setup.

4. **Customization:**  
You can customize the default responses and trigger phrases to better suit your language or personal preferences. Just ensure that any changes maintain the overall structure required for LLM integrations.

---

## Resources & Documentation

- **Spotify:** [https://open.spotify.com/](https://open.spotify.com/)
- **SpotcastV5 on GitHub:** [https://github.com/fondberg/spotcast/tree/dev](https://github.com/fondberg/spotcast/tree/dev)
- **ViewAssist on GitHub:** [https://github.com/dinki/view_assist_integration](https://github.com/dinki/view_assist_integration)
- **Home Assistant Blueprints Documentation:** [Home Assistant Blueprints](https://www.home-assistant.io/docs/automation/blueprint/)

---






