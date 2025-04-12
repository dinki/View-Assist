---
title: "Template Functions"
sidebar_position: 4
---

# Template Functions

View Assist has two custom template functions available to help with creating blueprints, automations and scripts.

## View Assist Entities

### Function Name
`view_assist_entites`

### Description
The function will return a list of View Assist sensor entity ids or attributes based on the passed filter or exclusions set.

### Parameters
filter (optional) - a json list of attribute values to include
exclude - a json list of attribute values to exclude
attr - the attribute to return instead of the entity id

### Examples
```
view_assist_entities()
view_assist_entities(filter={"type":"view_audio"})
view_assist_entities(filter={"type":"view_audio", "do_not_disturb": true})
view_assist_entities(filter={"type":"view_audio"}, attr="mode")
view_assist_entities(filter={"type":"view_audio"}, exclude={"mode":"hold"}, attr="mic_device")
```

## View Assist Entity

### Function Name
`view_assist_entity`

### Description
The function will return a View Assist sensor entity id from the value passed matching its main config entities/devices.

### Parameters
(required) - a string value matching any of the following:

- microphone entity id or device id
- media player entity id or device id
- music player entity id or device id
- display device id
mimic (optional) - to cause the return of the first View Assist instance set as a mimic if the required value does not match an entity.

### Examples
```
view_assist_entity("4a3389dfdc31e0c0fe451396ea741118")
view_assist_entity("media_player.my_media_player")
view_assist_entity("media_player.invalid_media_player", mimic=true)
```

This can be used within other functions as it returns a string entity id.
Ie.
```
state_attr(view_assist_entity("4a3389dfdc31e0c0fe451396ea741118"),"mode")
```