from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
)
from .const import DOMAIN
#import homeassistant.helpers.entity_registry as er
from homeassistant.helpers import entity_registry as er

import logging

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up View Assist from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    # Request platform setup
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

##################
# Get Target Satellite
# Used to determine which VA satellite is being used based on its microphone device
#
# Sample usage
# action: view_assist.get_target_satellite
# data:
#   device_id: 4385828338e48103f63c9f91756321df


    async def handle_get_target_satellite(call: ServiceCall) -> ServiceResponse:
            """Handle a get target satellite lookup call."""
            device_id = call.data.get("device_id")
            entity_registry = er.async_get(hass)

            entities = []

            entry_ids = [entry.entry_id for entry in hass.config_entries.async_entries(DOMAIN)]

            for entry_id in entry_ids:
                integration_entities=er.async_entries_for_config_entry(entity_registry, entry_id)
                entity_ids = [entity.entity_id for entity in integration_entities]
                entities.extend(entity_ids)

   
            # Fetch the 'mic_device' attribute for each entity
            # compare the device_id of mic_device to the value passed in to the service
            # return the match for the satellite that contains that mic_device
            target_satellite_devices = []
            for entity_id in entities:
                if state := hass.states.get(entity_id):
                    if mic_entity_id := state.attributes.get("mic_device"):
                        if mic_entity := entity_registry.async_get(mic_entity_id):
                            if mic_entity.device_id == device_id:
                                target_satellite_devices.append(entity_id)


            # Return the list of target_satellite_devices
            # This should match only one VA device
            return {"target_satellite": target_satellite_devices}

    hass.services.async_register(
        DOMAIN,
        "get_target_satellite",
        handle_get_target_satellite,
        supports_response=SupportsResponse.ONLY,
    )
#
#########


#########
# Handle Navigation
# Used to determine how to change the view on the VA device
#
# action: view_assist.navigate
# data:
#   target_display_device: sensor.viewassist_office_browser_path
#   target_display_type: browsermod
#   path: /dashboard-viewassist/weather
#
    async def handle_navigate(call: ServiceCall):
            """Handle a navigate to view call."""
            target_display_device = call.data.get('target_display_device')
            target_display_type = call.data.get('target_display_type')
            path = call.data.get('path')

            if not target_display_device or not target_display_type or not path:
                # Figure out how to write an error to the log
                 return
            
            if target_display_type == "browsermod" :
                await hass.services.async_call('browser_mod', 'navigate', {'entity_id': target_display_device, 'path': path})

    hass.services.async_register(
        DOMAIN,
        "navigate",
        handle_navigate
    )

#
########


    return True
    
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    if unloaded := await hass.config_entries.async_forward_entry_unload(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded
