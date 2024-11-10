This is a list of things to do and things done for the dashboard/ui upgrade

# To do


* Add new VA Assist listening CSS
* Use VA device assist bar type to determine which to show when called
* Look at both assisting and processing variants of the bar and popup
* Use microphone type to set variables in variable template of dashboard
* Update YAML template device config to reflect changes made making these unnecessary to define manually
* Give device id in YAML config so that device can have an area ??
* Update all existing full screen views to take up all available space
  * Camera
  * Webpage
* Consider option to handle icon bar list color (black or white) OR figure out how to add drop shadow on icons to ensure viewable on white backgrounds
* Document how to add button template for custom icons
* Document how to manipulate icon lists for developers
* Look at using default dashboard in VA device config so things like buttons can be more dynamic (weather button on clock screen)
* Fix restart HA goes to night mode when HA unavailable


# Done

* Change method for displaying icons using VA device attribute status_icons list (thanks @JimmyJamesBob)
* Proof of concept automation for adding/removing default icons (mic mute, speaker mute, do not disturb, hold mode)
* Test proof of concept icon display and automation with at least one user (thanks @JimmyJamesBob)
* Move existing bar to bottom of screen
* Set default z-index level for title and status areas so they are always above main card
* These views have changed:
  * Clock - use absolute positioning for date and time  
  * Music - default and alternative (thanks @JimmyJamesBob);
  * Alarm - Updated in beta repo      
* Test launch icons in status bar
* Incorporate proof of concept icon handling automation into device configuration blueprint
* Insure icon list is always defined.  Do this either in device configuration blueprint on startup, device configuration default or handle in icon handling sequences (aka update jinja to handle)
* Add default options (timeout, mode, do_not_disturb, background) to BP and set on start
* Add option to device configuration blueprint to allow users to set launch icons.  These will be added to the list on start up and never removed
* Add ability to set default background in device configuration blueprint and use in clock card.  Set on start
* Add select for listening CSS preference to device configuration blueprint and set on start up.  Choices are new (default) and existing bar
* Add select for microphone type (Stream Assist, HASSMic, Home Assistant voice satellite, other) to device configuration blueprint and set on start up
* Edit clock card to use default_background variable in VA device attributes

