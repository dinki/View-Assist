---
title: Xiaomi Smart Clock (X04G / LX04)
sidebar_position: 3
---

The Xiaomi Smart Clock is an Android based smart clock that runs Android Go 10. There are two variants: the LX04 for China (LX04) and the X04G for the rest of the world. They have the same hardware but LineageOS can only be installed on the X04G as the LineageOS image for this device assumes the X04G partition layout. Fortunately the LX04 can be flashed to the X04G.

This guide is based on:
- [Rainygortex3's XDA thread](https://xdaforums.com/t/guide-xiaomi-smart-clock-guide-to-convert-lx04-china-edition-to-x04g-global-edition-and-vice-versa.4665010/)
- [octathorp's XDA thread](https://xdaforums.com/t/xiaomi-mi-smart-clock-development-guide-gsi.4629771/)
- [octathorp's tools](https://github.com/octathorp/x04g_tools)
- [Informatic's research](https://github.com/Informatic/xiaomi-x04g-research)
- [AyraHikari's guide](https://github.com/AyraHikari/xiaomi-x04g-lx04/tree/main)

# Goal

The goal is to have the Xiaomi Smart Clock running View Assist Companion App. 

While you can get Android Go 10 running ViewAssist Companion App (VACA), it's more straightforward to get LineageOS running on the device and then have VACA run on it.

If you have a Chinese Market Smart Clock (LX04), first flash it to an X04G, then proceed to the LineageOS instructions.

If you have a rest-of-world clock (X04G) proceed to the LineageOS instructions.

# Necessary Software

## To Install LineageOS
- Download and install [mtkclient]( https://github.com/bkerler/mtkclient) to backup your device and flash it as necessary. Follow the instructions to install all its dependencies.
- Download and install the [Android SDK and Platform Tools](https://developer.android.com/tools/releases/platform-tools) for `adb` and `fastboot`.
- Download the [LineageOS image](https://androidfilehost.com/?fid=10620683726822080854)


## For LX04 -> X04G Conversion
- If you have an Chinese market clock (LX04) download the following files from AyraHikari's github repo: [boot1_for_microx04g.bin](https://github.com/AyraHikari/xiaomi-x04g-lx04/blob/main/files/boot1_for_microx04g.bin), [gpt_x04g.bin](https://github.com/AyraHikari/xiaomi-x04g-lx04/blob/main/files/gpt_x04g.bin), and [preloader_mico_x04g.bin](https://github.com/AyraHikari/xiaomi-x04g-lx04/blob/main/files/preloader_mico_x04g.bin) and the `Global Dump ROM Dump_mico_x04g.tar.xz` linked to from the [Tools section](https://github.com/AyraHikari/xiaomi-x04g-lx04/blob/main/convert-lx04-to-x04g.md#tools).


# Backup your Clock

**This is important, back up your clock. You will use files from the backup plus downloaded files to flash your clock to the new software.**

Regardless of which clock you have, use `mtkclient` to back up your clock first.

Follow [these instructions](https://github.com/octathorp/x04g_tools/blob/master/howtos/BackupFlash.md#mtkclient) to use mtkclient to back up the flash and partitions of your clock.

# China Edition (LX04) -> Global Edition (X04G) Instructions

1. Unlock the bootloader on the clock by running: 
```
python mtk.py da seccfg unlock
```
2. Flash the partition layout for the global edition (downloaded from AyraHikari's github) to the clock: 
```
python mtk.py wf {Replace this with the path to gpt_x04g.bin from github} --noreconnect
```
3. Flash the global edition partitions (unzipped from Global Dump ROM Dump_mico_x04g.tar.xz)to the clock: 
```
python mtk.py wl --preloader {Replace this with the path to preloader_mico_x04g.bin from github} --noreconnect {Replace this with the path to the unzipped Global Dump ROM Dump_mico_x04g.tar.xz}
```
4. Flash boot1 from the global edition (from AyraHikari's github) to the clock's preloader: 
```
python mtk.py w preloader {Replace this with the path to the downloaded boot1_for_microx04g.bin}  --parttype=boot1 --preloader {Replace this with the path to the downloaded preloader_mico_x04g.bin}
```
5. Erase the userdata, cache, and proinfo on the clock: 
```
python mtk.py e userdata,cache,proinfo
```
6. Write proinfo **from your backup** to the clock: 
```
python mtk.py w proinfo {Replace this with the path to your backed up original proinfo.bin}
```
7. Reset the clock: 
```
python mtk.py reset
```

Wait for the clock to fully boot to make sure the flashing worked. It will take some time to boot for the first time (on the order of minutes).

# Installing LineageOS on X04G

Installing LineageOS on your X04G is relatively easy (especially compared to going from LX04 -> X04G).

1. Unlock the clock's bootloader: 
```
python mtk.py da seccfg unlock
```
2. Flash the superimage
```
fastboot flash super super.img
```
3. Flash vbmeta: 
```
fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
```
4. Flash the boot image: 
```
fastboot flash boot boot.img
```
5. Reboot
```
fastboot reboot
```

Depending on various OS vagaries, you may need to manually set the clock to fastboot mode. Do so by:
1. Hold down the volume up and down buttons while you connect the clock to your computer. You will get to a `No Command` screen.
1. At the `No Command` screen, hold the Mute button and click the volume up button. Release the Mute button
1. Use the volume down button to highlight `Enter fastboot` and click the Mute button to select `Enter fastboot`
1. Use the volume buttons to highlight `Reboot to bootloader` and click the Mute button to select.

The clock will then reboot to fastboot mode and you can run the above commands. You will have to do this before each fastboot command if your computer won't force the clock into fastboot when running the `fastboot` command.

# Setting up ViewAssist Companion App in LineageOS.

## Booting LineageOS

Booting LineageOS on the clock will take a long time and will spend a period of time showing a white box on a black screen. This is expected.

## LineageOS Settings

There are a few settings that you should modify to expand the screen real-estate and enable ADB.

### Change screen size

1. Open Settings > Display > Display size and text and set Display size so that the slider is all the way to the left.

### Enable ADB

1. Open Settings > About device, scroll down to Build number and tap it until it says you're a Developer
2. Open Settings > System > Developer options, scroll down to USB debugging and disable and enable it so you have ADB enabled over USB.

### Reduce boot time

1. For some reason, the boot animation takes a lot of time. To reduce the boot time in half, install this Magisk Module [OEM boot animation](https://github.com/stelios333/x04g_bootanim/releases).

## Install the VACA app

1. From your computer while connected to the clock:
```
adb install {Replace this with the path to the VACA app}
```

## Set up VACA in Home Assistant
1. Adopt the VACA install on the Smart Clock in Home Assistant.
1. Set the gain as appropriate to your environment; I have set it to 0.
1. Set the wake word threshold as appropriate to your environment; I have it set to 8.

# You're done!
Enjoy!
