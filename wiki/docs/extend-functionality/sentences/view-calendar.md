# View Calendar

This blueprint allows the user to display any calendar listed in the configuration by using the defined command text. The trickiest part of the install is defining the dictionary option though it is not hard once you understand it:

```
all:
  - calendar.mom
  - calendar.dad
  - calendar.kid1
  - calendar.work
mom:
  - calendar.mom
work:
  - calendar.work
```

This is a dictionary. The format is the name associated with the calendars followed by the Home Assistant device name(s). Additional calendars can be added in a similar fashion as the example. You can have as many or as little as you like but you must have at least the calendar group `all`. This is the default calendar group to show when no specific calendar is requested. The `all` calendar will be shown when either no specific calendar is requested or as default if an unrecognized calendar group name is used.

## Requirements

Install [Calendar Card Pro](https://github.com/alexpfau/calendar-card-pro) via HACS

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
