# Locate a Person

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/jsittner/View-Assist/blob/locate-a-person/View_Assist_custom_sentences/Locate_a_Person/blueprint-locateaperson.yaml)

This blueprint enables you to track the location of a home assistant user on a map. The map display shows the geocoded address and the most recent location update timestamp. If you choose to hold the view, it will provide real-time updates as the tracking device sends new location data.

Requirements:
  * The Background location needs to be enabled. It can be found in the home assistant mobile app -> settings -> companion app -> Location sensors.
  * The Geolocation sensor needs to be enabled along with 'Update sensor with location sensors'. It can be found in the home assistant mobile app -> settings -> companion app -> manage sensors.  
  * Home assistant Background access also needs to be enabled. It can be found in the home assistant mobile app -> settings -> companion app -> other settings.
