# Details for Weather View

<a href="https://www.youtube.com/watch?v=H_hiLqBjQMk"><img src="https://img.youtube.com/vi/H_hiLqBjQMk/mqdefault.jpg" width="60%"></a>

Detailed install video:
https://youtu.be/H_hiLqBjQMk



This card can be added by copy pasting.  One variable in the configuration will need to be changed to reflect your weather entity

```
variables:
  var_forecast_entity: weather.home
```

If you are using the <a href="https://www.home-assistant.io/integrations/nws/">National Weather Service (NWS)</a> weather integration, you will also need to change the forecast_type (line 35) to be either "hourly" or "twice_daliy" due to the way the integration creates the forecast.
```
    card:
      type: weather-forecast
      entity: '[[[ return variables.var_forecast_entity ]]]'
      forecast_type: <strong>hourly</strong>
```

# Change log

June 14 2024
v1.0.2
Added instructions for NWS weather entities that don't have "daily" forecasts

June 10 2024
v1.0.1
Fix possible bad title

June 9 2024
v1.0.0
Initial release

