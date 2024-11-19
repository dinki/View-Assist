Instructions for installing the new dashboard for existing users:

* Back up your existing dashboard!  This is 100% not optional.
  * Go to your View Assist dashboard then click the pencil icon in the top right corner, then the three dots, then `Raw configuration editor`, then copy paste the entire contents into a text file and save this on your computer for safe keeping
* Copy the new dashboard code from [here](https://github.com/dinki/View-Assist/blob/viewassist-dashboard2.0/View%20Assist%20dashboard%20and%20views/dashboard/dashboard.yaml) onto your clipboard
* Go back to your dashboard editor from the step where you made the backup copy and CAREFULLY paste over the code from the beginning down to the last line before `views:` .  You are attempting to replace what exists above that line only.  Hit save
* You'll need to update the code for the following views to take advantage of the new functions if you are.  You only need to update views you are currently using or plan to use.  You can find these views [here](https://github.com/dinki/View-Assist/tree/viewassist-dashboard2.0/View%20Assist%20dashboard%20and%20views/views)
  *  Clock
  *  Music
  *  Alarm (if using the beta version has been updated)
  *  Webpage
  *  Camera
* Install the updated blueprint 
