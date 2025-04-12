---
title: "Custom Elements"
sidebar_position: 2
---

# Custom Elements

View Assist has two custom elements available to help with screen updates.  They can be placed in the button card as custom field values.

## Clock

This is designed to display a formatted datetime for clocks that updates every second, to overcome the limitations of Lovelace only updating when the entities atteach to cards update.

The viewassist_clock custom element has the following attributes
- `server_time`: (optional boolean, default true) - whether to use the server time for display
- `format`: (optional string, default %H:%m) - the format for the datetime output (follows python strftime formats)

### Examples

`<viewassist_clock server_time=true format='%H:%M'></viewassist_clock>`
12:15

`<viewassist_clock server_time=true format='%a, %e %b'></viewassist_clock>`
Fri, 28 Feb

## Countdown
This is designed to provide a countdown to a future datetime to overcome the limitations of Lovelace, not being able to update on a second interval for VA timer displays

The viewassist_countdown custom element has the following attributes
- `expires` - (required datetime) - a datetime that javascript can convert to a JS Date object
- `server_time` (optional boolean, default true) - define if the countdown uses server time to compare the expires
- `show_negative` (optional boolean, default true) - define if should display expired or negative countdown
- `no_timer_text` (optional string, default '') - define text to display if expiry is 0
- `expired_text` (optional stinrg, default '') - define text to display when timer has expired (if show negative is false)

If expires is null, the countdown will display No Timer.

### Examples

`<viewassist-countdown expires="2025-02-28T18:00:00Z"></viewassist-countdown>`

`<viewassist-countdown expires="${variables.var_timer_expiry}"></viewassist-countdown>`