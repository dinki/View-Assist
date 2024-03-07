# View-Assist
View Assist provides visual feedback for the Home Assistant Assist voice assistant using a collection of different automations, custom sentences, scripts, and extensions with the view being displayed on any Android device.  The project is at proof-of-concept (POC) phase but is fully functional.  

*WARNING* I am not a programmer I am just someone who knows just enough to be dangerous.  I am 100% certain that better ways exist than the way I am doing things and I am hoping that the HA community will continue to help improve this project through code submissions and comments in the issues section.

The information in this repo is separated into different subdirectories with additional readmes in each.  This project is designed so that you can pick and choose the parts that you want for your needs.  The custom sentences can be modified for those who may only be interested in voice only.  The dashboard views may be interesting to others who are writing their own custom sentences.

# Installation of software on Android device

An Android device is used for the display, voice input, and audio output.  The device used for the POC is a 2016 Amazon Fire 7HD tablet running Android 5.  It's because of this I am confident to say that this method should work on any device that is that old or newer.  The wake word detection is using the method where audio is constantly streamed back to the HA server which analyzes the audio and then Assist takes over after the wake word is found.

Credits:
The method for wake word on Android was discovered by watching the FixtSE video "Local Voice Assistant: Using your Cameras & Speakers in HA" https://www.youtube.com/watch?v=fP_BNFWLYnk

The following Android software has been used:

IP Webcam https://play.google.com/store/apps/details?id=com.pas.webcam

Fully Kiosk Browser & Lockdown  https://play.google.com/store/apps/details?id=de.ozerov.fully


-------

IP Webcam is used to stream the audio from the Android device to the HA server.  Download and install the app.  Scroll down and start server.  Allow all permissions

Enter the settings page and set:

Optional Permissions -> Allow streaming in background   Accept Android system permissions
Power management -> Turn on 'Disable notification' and 'Stream on device boot' 

This will allow for the IP Webcam app to stream audio/video to Stream Assist via RTSP.  This stream can also be used with HA as a webcam if you like as well.  I have not explored audio only streaming using this app but did note that Stream Assist may not work if video is not present.  You can lower resolution settings in the 'Video Prefences' section.

-------

Fully Kiosk Browser & Lockdown is used for the display and audio output.  The free version of the application will work for some functions but will display a watermark.  This is great for testing but for production you will more than likely want to support the developer by purchasing a license.  Money well spent.  Settings labeled (PLUS) require the license.

Download and install the app.  Go to settings.

Web Content Settings -> 
  Set 'Start URL' to your local HA server by name or your server address  (eg http://homeassistant.local:8123 or http://192.168.0.23:8123)
  Set 'Username' to your HA username
  Set 'Password' to your HA password
Advanced Web Settings ->
  Turn on 'Ignore SSL Errors'  You may not need to do this but my old tablet did show notifications when trying to show Wikipedia images
  Change color of 'Default Webview Background Color' to black or your favorite color
Universal Launcher ->
  Applications to Run on Start in Background (PLUS) choose 'Ip Webcam'
Remote Administration (PLUS) ->
  Turn on 'Enable Remote Administration'   This is needed to expose FK media player to Music Assistant addon

-------  
  
  
