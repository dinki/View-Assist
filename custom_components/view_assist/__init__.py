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


    async def handle_get_id(call: ServiceCall) -> ServiceResponse:
        """Handle a device lookup call."""
        hass: HomeAssistantType = call.hass
        entity_registry = er.async_get(hass)
        entity_id = call.data.get('entity_id')
        
        entity_entry = entity_registry.async_get(entity_id)
        if entity_entry and entity_entry.device_id:
            device_id = entity_entry.device_id
            return {"device_id": device_id}
        
        return {"error":  "Device ID not found"}

        # entity_id = call.data.get('entity_id')
        # state = hass.states.get(entity_id)
        # mic_device = state.attributes.get('mic_device')
        # display_device = state.attributes.get('display_device')
        # return {"mic_device": mic_device, "display_device": display_device}

    hass.services.async_register(
        DOMAIN,
        "get_id",
        handle_get_id,
        supports_response=SupportsResponse.ONLY,
    )

    async def handle_satellite_lookup(call: ServiceCall) -> ServiceResponse:
        """Handle a satellite lookup call."""
        device_id = call.data.get("device_id")
        return {"device_id_received": device_id}

    hass.services.async_register(
        DOMAIN,
        "get_satellite",
        handle_satellite_lookup,
        supports_response=SupportsResponse.ONLY,
    )
#####
# Working

    # async def handle_get_members(call: ServiceCall) -> ServiceResponse:
    #         """Handle a get members lookup call."""
    #         entity_registry = er.async_get(hass)

    #         entities = []

    #         entry_ids = [entry.entry_id for entry in hass.config_entries.async_entries(DOMAIN)]

    #         for entry_id in entry_ids:
    #             integration_entities=er.async_entries_for_config_entry(entity_registry, entry_id)
    #             entity_ids = [entity.entity_id for entity in integration_entities]
    #             entities.extend(entity_ids)

    #         return {"device_id_received": entities}


    async def handle_get_members(call: ServiceCall) -> ServiceResponse:
            """Handle a get members lookup call."""
            device_id = call.data.get("device_id")
            entity_registry = er.async_get(hass)

            entities = []

            entry_ids = [entry.entry_id for entry in hass.config_entries.async_entries(DOMAIN)]

            for entry_id in entry_ids:
                integration_entities=er.async_entries_for_config_entry(entity_registry, entry_id)
                entity_ids = [entity.entity_id for entity in integration_entities]
                entities.extend(entity_ids)

   
            # Fetch the 'mic_device' attribute for each entity
            # then get the entity registry entry for the mic entity id to get device id
            mic_devices = []
            for entity_id in entities:
                if state := hass.states.get(entity_id):
                    if mic_entity_id := state.attributes.get("mic_device"):
                        if mic_entity := entity_registry.async_get(mic_entity_id):
                            if mic_entity.device_id == device_id:
                                mic_devices.append(entity_id)


            # Return the list of mic_device attributes
            return {"mic_devices": mic_devices}

    hass.services.async_register(
        DOMAIN,
        "get_members",
        handle_get_members,
        supports_response=SupportsResponse.ONLY,
    )

#####

    return True
    
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    if unloaded := await hass.config_entries.async_forward_entry_unload(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded
