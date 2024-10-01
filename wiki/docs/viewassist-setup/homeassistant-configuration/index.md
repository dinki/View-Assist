---
id: haconfig
title: "Step Three: Home Assistant Configuration"
sidebar_position: 4
---

# Home Assistant Configuration

:::info
Note that these steps are only necessary if using View Assist with video enabled satellites.  It is not necessary to install these for voice only satellites.
:::

Several Home Assistant custom integrations (or custom_components as they are often referred to) are used for several pieces of the View Assist flow.  These can all be installed using the **Home Assistant Community Store (HACS)**.  If you do not have HACS installed, [visit the official documentation](https://hacs.xyz/docs/setup/prerequisites) for instructions and then return here to proceed.

**Required**

- **Stream Assist** - listens to audio coming from tablet to process wake word and pass to Assist Pipeline
- **set_state.py** - used to set states for the View Assist satellite devices

**Required for display capable satellites**
- **Browser Mod** - allows switching views and routing playback audio to your tablet

Additional Home Assistant integrations may be required for some custom sentence blueprints.  You will be advised on the detailed installation page which you may need.  These will be stored in the 'Optional' section and should be skipped until needed.

