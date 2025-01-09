---
title: Using Immich-Kiosk as Clock Background
sidebar_position: 1
---
​
​
For anyone looking to set immich-kiosk as their clock background, this is how the view can be modified:
​
```
type: custom:button-card
variables:
  var_url: "url to immich-kiosk or other hosted slideshows."
  clockcardversion: 1.1.0
template:
  - variable_template
  - body_template
styles:
  grid:
    - grid-template-areas: |
        "title status"  
        "time time"
        "date date"
        "assist assist"
    - grid-template-rows: min-content min-content min-content min-content
    - grid-template-columns: 1fr 1fr
  card:
    - background-color: "#00000"
    - border-width: 0px
    - border-radius: 0px
  custom_fields:
    message:
      - font-size: "[[[ return variables.var_font_size ]]]"
      - align-self: center
      - justify-self: center
      - height: 100%
      - width: 100%
      - position: absolute
      - justify-content: center
      - text-align: start
    time:
      - justify-self: center
      - z-index: 1
      - font-size: 55vh
      - font-weight: bold
      - position: absolute
      - color: white
    date:
      - justify-self: center
      - align-self: center
      - z-index: 1
      - font-size: 15vh
      - width: max-content
      - position: absolute
      - top: 70%
    night:
      - position: absolute
      - min-height: 200%
      - width: 200%
      - backdrop-filter: brightness(10%)
      - overflow: hidden
      - display: >-
          [[[ try {if
          (hass.states[variables.var_assistsat_entity].attributes.mode ===
          "night") return "block"; else return "none";} catch { return 
          "none"}
            ]]]      
      - z-index: 2
custom_fields:
  message:
    card:
      type: iframe
      url: "[[[ return variables.var_url ]]]"
      aspect_ratio: 50%
  title:
    card:
      type: custom:button-card
      icon: "[[[ return variables.var_weather_icon ]]]"
      name: "[[[ return variables.var_weather_temperature ]]]"
      tap_action:
        action: navigate
        navigation_path: weather
      styles:
        card:
          - background-color: transparent
          - border-width: 0px
          - width: 50%
          - margin-left: 5%
          - margin-top: "-5%"
        grid:
          - grid-template-areas: "\"i n\""
          - grid-template-rows: min-content min-content
        name:
          - font-size: 15vh
          - color: white
        icon:
          - width: 25vw
          - color: white
  time: "[[[ return variables.var_current_time ]]]"
  date: "[[[ return variables.var_date_short ]]]"
  night: .
```
​
You will need to modify the `var_url` variable to have the path to your slideshow url