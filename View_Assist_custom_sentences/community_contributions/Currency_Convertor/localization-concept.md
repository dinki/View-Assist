# Localization Concept

## Description of the problem

The ViewAssist automations contain language input/output and screen output texts in many places. The phrases for triggering the automation can still be customized to your own language when executing the blueprint.  
However, the speech and screen texts are hard-coded into the automation. To change them, you must take control of the automation to edit the texts in the Visual Editor or in the YAML code.  
The same applies to adjusting the phrases that trigger the automation, e.g. if additional phrases are to be included.

Taking control separates the automation from the original blueprint. Updating the blueprint then requires deleting the detached automation and then re-adjusting the newly created automation to the blueprint.

To make a ViewAssist automation available for different languages, you must create language-specific blueprints or remove the language input/output and screen output texts from the blueprint and make them available elsewhere.

## Basics of Home Assistant

Home Assistant Assist uses [localized language files](https://github.com/home-assistant/intents/tree/main?tab=readme-ov-file) in yaml format to handle BuildIn Intents. These BuildIn Intents can be [extended](https://www.home-assistant.io/integrations/conversation/) for both speech input and speech output.  
Additional [Custom Intents](https://www.home-assistant.io/voice_control/custom_sentences/) can be added via automation and via intent scripts.

ViewAssist also uses speech as a trigger in automations. The issues with this have already been discussed.

For intent handling with intent scripts, YAML files are used that contain localized phrases for triggering an intent and provide localized phrases for a response after the intent has been executed. The intent itself is handled in [Intent Scripts](https://www.home-assistant.io/integrations/intent_script/). A card template can be used for text output and a speech template for voice output.

However, the functionality is not as extensive as in ViewAssist. For example, it is not possible to customize variables using a template. It is also not possible to control the speech and screen output on individual devices, as ViewAssist prefers.

## Concept for localizing ViewAssist

The following concept describes a way to separate the blueprint from the language components and thus a simple way to make it easy to localize ViewAssist. The implementation of the concept is explained using the ViewAssist automation **CurrencyConvertor** as an example.

The concept combines the localization of Home Assistant Assist with the functionality of ViewAssistant.

The phrases for the **voice control** of a ViewAssist automation are extracted from the blueprint and transferred to the localized **custom_sentences**. The hard-coded texts for the **voice and text output** are removed from the automation and inserted into the **response_sentences**.

The **intent handling** is controlled by an associated **intent_script**. In this script the intents of the *custom_sentences* are published with a **MQTT call**. There is no screen or voice output in the *intent_script*.

The associated **ViewAssist automation** is no longer triggered by a **sentence trigger** but by a **mqtt trigger**. In the automation, the respective functionality is executed as before, with the exception of the speech output. Since the *mqtt trigger* does not recognize a **conversation response** variable, this is replaced by calling a separate **response_handler** which generates the speech output for a **media_player.play_media** action and the speech and screen output based on the **response_sentences**.

### Custom Sentences

The triggering phrases of an automation are stored in yaml files under
> {conf_dir}/custom_sentences/{language}/{sentences.yaml}

*conf_dir* is the root directory, which differs depending on the HA installation type. For an HA OS installation, this would be the /config directory. All yaml files under *custom_sentences* are evaluated for intent handling.

Since the custom_sentences directory does not allow any subdirectories other than the localization directories, the filenames should follow the scheme
> viewassist-{automation_name}.sentences.yaml

in order to enable faster retrieval.

The following example shows the English *custom sentences* for the currencyconvertor. The file is stored under 
> {conf_dir}/custom_sentences/**en**/viewassist-currencyconvertor.sentences.yaml

```
language: "en"
intents:
  ConvertCurrency:
    data:
      - sentences:
          - "How much is {fromcurrency} in {tocurrency}"
          - "convert {fromcurrency} to {tocurrency}"
        response: "convert"
        requires_context:
          area:
            slot: true
  ExchangeCurrency:
    data:
      - sentences:
          - "What is the exchange rate for {tocurrency}"
        response: "exchange"
        requires_context:
          area:
            slot: true

lists:
  fromcurrency:
    wildcard: true
  tocurrency:
    wildcard: true
```

The file contains two intents named **ConvertCurrency** and **ExchangeCurrency** and the triggering phrases. The phrases contain variables, here **fromcurrency** and **tocurrency**, which are passed to the *Home Assistant Intent Handler*. In addition, the required context is created with the **area** variable. The **area** variable contains the area for the triggering device. Under **lists** it is specified that in this case **fromcurrency** and **tocurrency** can contain any characters. The variable names are freely selectable, but the variable names **{name}** and **{area}** are used internally by the Home Assistant Intent Handler.

An existing language file can be copied for a new localization. The variable **language** must be adapted and the phrases must be replaced with the localized form. All variables in the phrases must be used, but their order is interchangeable. A German version would look like this, stored under
> {conf_dir}/custom_sentences/**de**/viewassist-currencyconvertor.sentences.yaml

```
language: "de"
intents:
  ConvertCurrency:
    data:
      - sentences:
          - "Wieviel sind {fromcurrency} in {tocurrency}"
          - "Wechsel {fromcurrency} in {tocurrency}"
        response: "convert"
        requires_context:
          area:
            slot: true
  ExchangeCurrency:
    data:
      - sentences:
          - "[Wie ist] [der] [Umrechnungs|Wechsel]kurs [für|von] {tocurrency}"
        response: "exchange"
        requires_context:
          area:
            slot: true

lists:
  fromcurrency:
    wildcard: true
  tocurrency:
    wildcard: true
```
### Intent Handling
Intent handling is started by an **intent_script**. To be able to use a variety of Intent scripts, they are stored under
> {conf_dir}/intent_script/{intent_script.yaml}

To ensure that Home Assistant also used this directory, the **configuration.yaml** must contain the entry
```
intent_script: !include_dir_merge_named intent_script/.
```

Since the intent_script directory does not allow further subdirectories, the filenames should follow the scheme
> viewassist-{automation_name}.intent.yaml

for faster retrieval.

The following example shows the intent file for the currencyconvertor:

```
ConvertCurrency:
  action:
    - action: mqtt.publish
      data:
        topic: viewassist/intent/currencyconvertor
        qos: "1"
        retain: false
        payload: >-
          {"intent": "convert",
           "fromcurrency": "{{ fromcurrency }}",
           "tocurrency": "{{ tocurrency }}",
           "devices": "{{ area_devices(area) }}"
          }
ExchangeCurrency:
  action:
    - action: mqtt.publish
      data:
        topic: viewassist/intent/currencyconvertor
        qos: "1"
        retain: false
        payload: >-
          {"intent": "exchange",
           "tocurrency": "{{ tocurrency }}",
           "devices": "{{ area_devices(area) }}"
          }
```
In this file, a processing routine is stored for each intent of the custom Sentences. In the View Assist example, this is a call to the **mqtt.publish** action, which sends the contents of the variables from the custom phrases as a payload to the topic
> viewassist/intent/currencyconvertor

The topic name is basically arbitrary, but should follow the scheme
> viewassist/intent/{automation name}

> "intent": "convert  
> "intent": "exchange

passes the triggering intent names to be evaluated by the automation. Long names have been deliberately used for intent handling in order to keep track of a large number of intent files.

Only **limited templates** are possible within the yaml file. For this reason
> "devices": "{{ area_devices(area) }}"

can only be used to get a list of devices in an area, not the device_id of the triggering device itself.

Without the Speech and Card statement, the Intent script ends after this actions.

### Automation
Further Intent handling takes place in the automation. The automation for the currencyconvertor example is shown in the snippets below.

The mqtt trigger starts the automation.

```
trigger:
  - platform: mqtt
    topic: viewassist/intent/currencyconvertor
condition: []
action:
  - variables:

...

      target_satellite_device: |-
        {% for sat in expand(group_entity) %}
          {% if (device_id(sat.attributes.mic_device) in trigger.payload_json['devices'] ) or (device_id(sat.attributes.display_device) in trigger.payload_json['devices'] ) %}
            {{ sat.entity_id }}
          {% endif %}
        {% endfor %}
      target_display_device: "{{ device_id(state_attr(target_satellite_device, 'display_device')) }}"
      target_mediaplayer_device: "{{ state_attr(target_satellite_device, 'mediaplayer_device') }}"
      target_satellite_device_type: "{{ state_attr(target_satellite_device, 'type') }}"
    enabled: true
```

The topic name used in the intent script must be used in the trigger's **topic**.

In the **variables**, the *device* variable of the payload can be used to determine the associated **device_id**. Since the payload is generated in JSON format in the intent script, **trigger.payload_json** must be used in the automation.

The *payload* data can also be used later in the automation. In the current example, the values of **intent** and **tocurrency** are used to call the *currencyconvertor* script.

```
...

  - choose
      - conditions:
          - condition: template
            value_template: "{{ trigger.payload_json['intent'] == 'exchange'}}"
        sequence:
          - action: pyscript.currencyconvertor
            data:
              rapidapikey: "{{ rapidapikey }}"
              currencyto: "{{ trigger.payload_json['tocurrency'] }}"
            response_variable: conversion_response
...
```

As a result, the action with the *response_variable* **conversion_response** returns a dictionary with data that can be used by the speech and screen output.

### Response Sentences
Since the **intent script** ends after the mqtt action and the mqtt trigger does not know the **set_conversation_response** variable, a separate response handler is used. For this purpose, the automation calls the **response_handler** action, which was introduced with the **viewassist-response_handler.py** script. In the currencyconvertor example, this happens after the *pyscript.currencyconvertor* action mentioned above.

```
          - if:
              - condition: template
                value_template: "{{ conversion_response['error'] == 0 }}"
            then:
              - action: pyscript.response_handler
                data:
                  intent: ExchangeCurrency
                  response: speech
                  custom: viewassist-currencyconvertor
                  basecurrency: "{{ conversion_response['data']['from'] }}"
                  exchange: "{{ conversion_response['data']['value'] | round(2) }}"
                  exchangecurrency: "{{ conversion_response['data']['to'] }}"
                response_variable: response_speech
```

The **response_handler** expects the variables **intent**, **response**, and **custom**.

```
@service(supports_response="optional")
def response_handler(intent=None, response=None, custom=None, **kwargs):
```

All other variable names and the number of variables are arbitrary and are passed to __**kwargs__. However, they must be based on the contents of the **response_sentences** that use those variable names.

The response sentences of an automation are stored in localized yaml files under
> {conf_dir}/custom_sentences/{language}/{automation_name}.response.yaml

Using the currencyconverter example and the English version, this is the file
> {conf_dir}/custom_sentences/en/viewassist_currencyconverter.response.yaml

```
language: "en"
responses:
  intents:
    ConvertCurrency:
      speech: "{amount} {fromcurrency} converts to {convert} {tocurrency}"
      screen: "{amount} {fromcurrency} converts to {convert} {tocurrency}"
    ExchangeCurrency:
      speech: "The  exchange rate to {exchangecurrency} is {exchange}"
      screen: "The  exchange rate from {basecurrency} to {exchangecurrency} is {exchange}"
```

The file contains sentences for each **intent** response, which are provided with one or more freely selectable **response** names. This makes it possible, for example, to use different texts for speech and text output. The **custom** variable of the script is used to select the yaml file based on the associated automation. Localization is done by evaluating the **hass.config.language** variables in the script.

The response_variable **response_speech** contains a dictionary with an **error** number and the localized text **message**.

### Speech
As a replacement for using the **set_conversation_response** variable, speech output is controlled by the **media_player.play_media** action.

```
...
              - action: media_player.play_media
                target:
                  entity_id: "{{target_mediaplayer_device}}"
                data:
                  media_content_id: >-
                    media-source://tts/{{
                    tts_device}}?message={{response_speech['message'] | replace(" ", "+")}}&language={{
                    tts_language}}&voice={{tts_model}}
                  media_content_type: provider
                enabled: true
...
```
The **message** value of the above response variable **response_speech** is used for the output. The variables **tts_device**, **tts_language** and **tts_model** are set in the Blueprint and should be the same as the selected **TTS component** of the Assist Pipeline. For the **media_content_id**, please note that spaces are replaced with a (+)-sign when generating the URL.

### Screen
The screen output has basically not changed. As explained earlier, a separate localized message can be generated for the text output that differs from the voice output.

In the example, the name of the currency is used for the voice output and the currency code is used for the screen output.

```
...
              - action: pyscript.response_handler
                data:
                  intent: ExchangeCurrency
                  response: speech
                  custom: viewassist-currencyconvertor
                  exchange: "{{ conversion_response['data']['value'] | round(2) }}"
                  exchangecurrency: "{{ trigger.payload_json['tocurrency'] }}"
                response_variable: response_speech
              - action: media_player.play_media
...
                  - action: pyscript.response_handler
                    data:
                      intent: ExchangeCurrency
                      response: screen
                      custom: viewassist-currencyconvertor
                      basecurrency: "{{ conversion_response['data']['from'] }}"
                      exchange: "{{ conversion_response['data']['value'] | round(2) }}"
                      exchangecurrency: "{{ conversion_response['data']['to'] }}"
                    response_variable: response_screen
                  - action: python_script.set_state
...
```

### Blueprint
The input definition in the blueprint depends on the application. Certain inputs must be present in all ViewAssist automations that want to use the localization described above. The extract from the currencyconvert blueprint shows the required entries:

```
blueprint:
  name: View Assist - Currency Convertor
  description: Convert currency from one type to another (View Assist Currency Convertor v 0.2.0)
  domain: automation
  input:

...

    tts_device:
      name: Text to Speech Device
      description: Your TTS Device to play media
      default: tts.piper
    tts_language:
      name: Text to Speech language
      description: Your preferred language for TTS
      default: en_US
    tts_model:
      name: Text to Speech voice model
      description: Your preferred voice model for TTS
      default: en_US-amy-medium
    group_entity:
      name: Group Entity
      description: The group that holds the list of View Assist satellites(example
        group.viewassist_satellites)
      selector:
        entity:
          filter:
          - domain:
            - group
          multiple: false
      default: group.viewassist_satellites
    view_path:
      name: Dashboard Info view
      description: The View Assist dashboard view to use for displaying information (example /dashboard-viewassist/info)
      default: /dashboard-viewassist/info

```

In addition to the **group_entity** to select the group of satellites and the **view_path** to select the dashboard view, entries for the **tts_device**, the **tts_language** and the **tts_model** are required. These entries should be similar to those in the Assist pipeline to allow consistent language output. The necessary combinations can be derived from the [Piper Github](https://github.com/rhasspy/piper/blob/master/VOICES.md).
They are then made available to the automation in the variable declaration in the trigger.

```
...

trigger:
  - platform: mqtt
    topic: viewassist/intent/currencyconvertor
condition: []
action:
  - variables:

...

      tts_device: !input tts_device
      tts_language: !input tts_language
      tts_model: !input tts_model
      group_entity: !input group_entity
      view: !input view_path
...
```

That's all. Give it a try :-)
