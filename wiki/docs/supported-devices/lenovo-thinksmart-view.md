---
title: Lenovo Thinksmart View
sidebar_position: 1
---

The Lenovo Thinksmart device is a nice Android tablet with a nice sounding speaker at an unbelievably low price (~$40 USD).  https://amzn.to/4bRBnhk

This set up is not for the faint at heart.  You have been warned. 

Special thanks to @mattmon and @endlessvoid on their work on this project and their help and listening ear while I got through this.


***

**UPDATE** A new ROM was release recently and it has become the preferred ROM.  You may want to consider using it instead of this ROM as the new one has far fewer problems.  See this guide for installing:  https://github.com/pgale/lineage_15.1_Installation_TSV

***


Find the original thread here with tons of useful information:

https://community.home-assistant.io/t/is-this-the-perfect-standalone-tablet-for-ha/658422

Start by watching this video.  I'm setting the link at the install procedure:

https://www.youtube.com/watch?v=V7CMizEOT-0&t=533s


This video shows the actual flashing process:

[![Image](https://img.youtube.com/vi/MMvEpfNmyUk/mqdefault.jpg)](https://www.youtube.com/watch?v=MMvEpfNmyUk)

Detailed install video:
https://youtu.be/MMvEpfNmyUk

Here's a video I created showing how to set up the software needed to use with View Assist.

[![Image](https://img.youtube.com/vi/-tiXUjK-hC4/mqdefault.jpg)](https://www.youtube.com/watch?v=-tiXUjK-hC4)


# Step by Step (by @mngarchow) to Flash firmware and setup for Windows

## Download Files
1. Download the prerequisite programs to do the flashing: https://bit.ly/3HOIr1g or https://mega.nz/file/EBQ3VSxK#X4DJmfPoFFEAxe8DxIqAIKQershp0Z_dVq-ZXFQ3Vyg
2. Use this ROM instead of the one mentioned in the first video: https://s3.us-east-1.wasabisys.com/filestash-buk/lenovo-thinksmart-view/combined_kingston_a11_gogapps.7z
3. (optional) Install 7Zip as needed so you can open the other downloaded files. (https://www.7-zip.org/download.html)

## Extract files and install Prerequisites
1. (optional) Create a directory on your desktop called ThinkSmartView
2. Extract the downloaded ThinkSmartView.zip to the ThinkSmartView folder
3. Extract the contents of the file combined_kingston_a11_gogapps.7z to a new folder in the ThinkSmartView folder called combined_kingston_a11_gogapps
4. Install the Qualcomm Drivers
	1. Double click the file QDLoader HS-USB Driver_64bit_Setup.exe
	2. Yes to the User Account Control prompt
	3. Leave everything as default, click Next a few times
	4. Choose WWAN-DHCP is not used to get IPAddress
	5. Next
	6. Accept license, Next
	7. Install
	8. Finish
	9. Restart PC when prompted at the end.
5. Install QPST 
	1. Open the QPST 2.7.496 folder
	2. Double click the file QPST.2.7.496.1.exe
	3. Yes to the User Account Control prompt
	4. If prompted, install the VC++ 2013 Redistributable by clicking Install
	5. When prompted, click Next 
	6. Click I accept, then Next
	7. Click Next two more times. Then click Install
	8. Click Finish when done.
6. Install ABD & Fastboot ++
	1. Double click the file ADB-and-Fastboot++\_v1.0.8.exe
	2. Yes to the User Account Control prompt
	3. Click I accept, then Next
	4. Click Next again.
	5. Leave the checkboxes for desktop shortcuts and Add to System Path options, then click Next.
	6. Click Install.
	7. Uncheck Open the Toolkit and Launch ADB & Fastboot++ options, click Finish.

## Flash ROM to device (make sure to use a usb 2.0 port, black not blue, and must use a usb 2.0 hub/bus in windows device manager too)
0. Open the QFIL tool (click Start then search for QFIL)
1. Under Select Build Type, pick Flat Build 
2. Under Select Programmer, browse to the ThinkSmartView\combined_kingston_a11_gogapps folder and select: prog_emmc_firehose_8953_ddr.mbn
3. Under Select Flat Build, click the Load XML button.
4. Navigate to the file rawprogram0.xml and click Open
5. Another file prompt window will open, select patch0.xml and click Open
6. Unplug the device power cable, plug the usb-c into the computer and the device. (This can be difficult to do for one person, get help as needed)
7. Hold down both volume buttons while simultaneously plugging in the power. You will hear windows make a sound to indicate it is connected. Let go of volume buttons when you hear the sound.
8. In QFIL, click on Select Port.
9. Select the Qualcomm device and click OK. (COM port number will be different for everyone)
10. Click the Download button and wait while the flasher downloads to the device. It will indicate successful when completed.
11. Unplug the ThinkSmartView, wait a moment, then plug it back in while holding only the volume up button. 
12. In the android recovery menu, press the volume up button until you get to Wipe Data/Factory Reset.
13. Press the volume down button to select Wipe Data/Factory Reset. When prompted "Are you sure?" press volume up to highlight Yes then volume down to select Yes. This will format the data and cache partitions.
14. When done, it will automatically highlight "Reboot System Now". Press volume down to select and reboot the device. 
15. The device will boot up with the new ROM installed. A Disney ducks image will display while the device boots. 
16. The device setup screen will display once boot is completed. Unplug the usb cord. 

## Configure
1. Starting on the device setup screen, tap START.
2. Skip
3. Set up wifi
4. Copy Apps and Data, choose Don't Copy.
5. Sign in with your google account and password.
6. On the protect your phone screen, choose Not Now and confirm by choosing Skip Anyway.
7. Choose No Thanks to Google Assistant
8. Choose No Thanks
9. Now on the device home screen.
10. Go to Settings (swipe up) > About Phone > tap on build number at least 7 times to open Developer Mode.
11. Tap Back > System > Advanced > Developer Options > Smallest Width
12. Set Smallest Width to 600
13. Back to settings
14. Settings > Security > Screen Lock > None 
15. Settings > Display > Screen timeout > 30 minutes
16. Done with this section, go back to the home screen.

## Install Apps
1. Open the Play Store
2. Search for WebView System Android
3. Pick Android System WebView beta and Install
4. Open the App, Change Provider, choose the 2nd option to allow it to use the new Webview installed instead of the stock application.
5. Press the home button to go back to home.
------------------


From this point you should be booted into the tablet.  

* Do not set any apps to autostart.  I had issues where the device would fail to boot after making that change causing a bunch of extra work to get back to where I was before.  Use Android app AutoStart Manager and use it to auto launch the applications you will be running. UPDATE: This advice may not be applicable.  I am still trying to sort why the device fails to boot and I think it is tied to wifi.  

*UPDATE* User @flab offers a suggestion:

> Turning off auto connect in WiFi settings seems to solve the reboot to Lenovo logo issue. If you or anyone else does find themselves stuck on the Lenovo logo boot screen, you can get around having to do a factory reset by just leaving the device unplugged for a few minutes and then trying again. Leaving it unplugged seems to give more time in the lock screen dance described at then end of your linked wiki.

This page may be helpful in finding the right place to turn off auto connect:  https://github.com/dinki/View-Assist/wiki/Find-IP-of-Android-device#note-you-may-want-to-turn-off-auto-connect-to-perhaps-lessen-wifi-boot-issues-if-using-the-lenovo-thinksmart-device

Additionally, I've found that after leaving the device unplugged you can quickly turn off the wifi and it will not crash to Lenovo.  That may not be necessary either.  Perhaps just unplugging for a few minutes is enough.

Multiple devices?  You may need to change the MAC address on additional to avoid wifi issues


## Change MAC address of WiFi interface on the Lenovo ThinkSmart device (credit @mllockwood)



(These instructions assume you already have the Windows applications installed and setup for ADB commands)

- Make sure the USB cable is connected between the Lenovo device and your PC.
- Open the ADB and Fastboot ++ program in Windows (already open from above steps)
- Create a folder in Windows. I created it in C:\LenovoThinkSmart as shown below in the path.
- Copy and paste each of these commands in to the command line:

```
adb root
adb pull /vendor/firmware/wlan/qca_cld/WCNSS_qcom_cfg.ini C:\LenovoThinkSmart
```

- A file named WCNSS_qcom_cfg.ini will be copied from the Lenovo device to C:\LenovoThinkSmart
- Open the file in Windows Notepad
- Locate the line that is:

```
# Each byte of MAC address is represented in Hex format as XX

Intf0MacAddress=000AF58989FF
```

- Change the "FF" at the end of the MAC address to another unique number.
- For example, I use "01" for my first Lenovo device, and "02" for the second, "03 for third, and so on...
- Save the WCNSS_qcom_cfg.ini
- Go back to the ADB and Fastboot ++ program.
- Type "exit" to get back out to the Windows command line and out of ADB shell.
- Copy and paste each of these commands in to the command line:

```
adb root
adb remount
adb push C:\LenovoThinkSmart\WCNSS_qcom_cfg.ini /vendor/firmware/wlan/qca_cld/
```

- You should see an indication that 1 file was successfully uploaded to the Lenovo device......

"C:\LenovoThinkSmart\WCNSS_qcom_cfg.ini: 1 file pushed, 0 skipped. 21.2 MB/s (14421 bytes in 0.001s)"

- Unplug the device.
- Push and hold the VOL + button
- Plug in power adapter to Lenovo device (no Windows sound heard this time)
- Recovery screen should be visible.
- Use VOL + to select "Wipe cache partition"
- Use VOL - to confirm
- Use VOL + to select "Yes"
- Use VOL - to confirm
- Use VOL - to confirm "Reboot system now"
- The Lenovo device will reboot.
- As the device is rebooting, you will see the Donald Duck in the car image.

Additional information here:
https://community.home-assistant.io/t/is-this-the-perfect-standalone-tablet-for-ha/658422/581


------------

Watch this page for updates.  The device has been really stable short of these boot oddities







