This is a list of things to do and things done for the dashboard/ui upgrade

# To do

* Incorporate proof of concept icon handling automation into device configuration blueprint
* Add new VA Assist listening CSS
* Add select for listening CSS preference to device configuration blueprint.  Choices are new (default) and existing bar
* Move existing bar to bottom of screen
* Update all existing full screen views to take up all available space
  * Clock - use absolute positioning for date and time
  * Alarm - use absolute positioning for snooze and dismiss buttons
  * Weather - also look at clipping
  * Music - default done (thanks @JimmyJamesBob); alternative done (?)
  * Sports
  * All Cameras (custom)
  * Camera
  * Intent
  * List
  * Webpage
  * Thermostat - also look at making larger
* Set default z-index level for title and status areas so they are always above main card
* Consider option to handle icon bar list color (black or white) OR figure out how to add drop shadow on icons to ensure viewable on white backgrounds
* Test launch icons in status bar
* Add option to device configuration blueprint to allow users to set launch icons.  These will be added to the list on start up and never removed
* Document how to add button template for custom icons
* Document how to manipulate icon lists for developers


# Done

* Change method for displaying icons using VA device attribute status_icons list (thanks @JimmyJamesBob)
* Proof of concept automation for adding/removing default icons (mic mute, speaker mute, do not disturb, hold mode)
* Test proof of concept icon display and automation with at least one user (thanks @JimmyJamesBob)
* Update all existing full screen views to take up all available space
  *  Locate
