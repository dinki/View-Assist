# 🎭 View Assist — Custom Prompt Avatars

This feature adds the ability to **select an avatar as a custom wake-word prompt**, allowing it to respond in *any language, voice, or TTS service* with **personalized random TTS responses**.  

Each avatar is represented through animated GIFs that appear on the screen when the wake word is detected.  
The included **blueprint** handles synchronization between the satellite microphone, the avatar animations, and the TTS greeting message.

---

## 🧠 How it works

When the wake word is detected:
1. The blueprint mutes the microphone for about **1.5–2 seconds**.
2. It plays a **custom random TTS greeting message**, such as:
   - “How can I help you?”
   - “Yes, I’m listening.”
   - “How can I assist you?”
3. The avatar’s **speech GIF** is shown during playback, then transitions to the **listening GIF**.
4. Once playback is finished, the blueprint **unmutes the microphone**, ready to capture your command.

This allows a natural and personalized interaction flow between the user and the assistant.

---

## ⚙️ Pre-requisites

- **Home Assistant 2025.11.1 or newer**
- A [configured voice assistant in Home Assistant](https://my.home-assistant.io/redirect/voice_assistants/) with STT and TTS in your preferred language
- The [View Assist Integration](https://github.com/dinki/view_assist_integration) installed, with all dependencies
- An audio streaming integration with microphone mute/unmute capability  
  For Android tablets, it’s recommended to use the [View Assist Companion App](https://github.com/msp1974/ViewAssist_Companion_App)

---

## 📦 Installation

### Step 1 — Copy overlay files

Copy the **`custom_overlays`** folder and the desired files into your Home Assistant configuration:

`/config/view_assist/`


Be careful **not to confuse this with** `/config/custom_components/view_assist/`.  
Inside `custom_overlays`, you’ll find:

- `overlay.css` — controls animation timing and display
- `overlay.html` — defines which avatars are shown
- Avatar GIFs (each avatar has two GIFs:  
  `<name>_speech.gif` and `<name>_listen.gif`)

If you don’t want to copy the full folder (to save space), you can manually create:
`/config/view_assist/custom_overlays/` directory

Then:
1. Copy `overlay.css`
2. Copy `overlay.html` and **uncomment** only the sections for the avatars you wish to use
3. Copy the corresponding GIFs for those avatars

Finally, **restart Home Assistant** or reload YAML files.

---

### Step 2 — Configure your avatar in View Assist

Open **Settings → Dashboard Options → Display Settings → Assist Prompt**,  
and select the avatar you’ve activated.

---

### Step 3 — Install and set up the Blueprint

Import and install the blueprint:  
👉 [Custom Prompt Responses](https://github.com/dinki/View-Assist/tree/dev/View_Assist_custom_sentences/community_contributions/Avatar_Prompt_Responses)

Then, configure the fields as follows:

- **Assist Satellites** → Select **all satellites** you want to use the custom responses with.  
- **Custom Responses** → Add short random responses, e.g.:

How can I help you?

Yes, I'm listening.

How can I assist you?

*Keep them short (1.5–2s playback) for synchronization with the avatar animation.*

---

### Step 4 — Set up your TTS URL Template

You can use **any TTS service** for the *TTS URL Template*.  
Here’s a simple trick to find the correct format for your setup:

1. Go to **Developer Tools → Actions**  
2. Choose the service **`media_player.play_media`**
3. Select a speaker under **Target**
4. Under **Media**, click **Pick media**
5. Choose a **TTS service**, **language**, and **voice**, then type a short test message
6. Switch to **YAML mode** — you’ll see the field `media_content_id` — that’s your **TTS URL**
7. Copy that URL, and replace the message text inside it with:
{{ custom_responses | random }}
8. Paste the full modified URL into the blueprint’s **TTS URL Template** field

This method works with **any language**, **any voice**, and **any number of custom messages**, making it extremely flexible.

---

### Step 5 — Microphone synchronization

- **Microphone Active State**  
- Set to **on** if your microphone entity is active when the switch is ON.  
- However, if your switch controls *mute*, then ON may actually mean “muted.” Adjust accordingly.

- **Microphone Reactivation Delay (seconds)**  
- Adjust this value so the microphone reactivates **just after** the greeting message finishes.  
- If the delay is too short, part of the greeting may be captured and confuse the STT.  
- If too long, the beginning of the user’s command might be missed.

---

## ✅ Summary

Once set up, your system will:
- Detect the wake word
- Show the chosen animated avatar
- Play a random personalized TTS greeting
- Reactivate listening smoothly  
…all synchronized for a natural, multilingual experience.

Enjoy creating your own avatars and personalities for your assistants!

---

*Created by [@relust](https://github.com/relust) for the [View Assist Integration](https://github.com/dinki/view_assist_integration).*
