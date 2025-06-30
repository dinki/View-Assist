# Device Functions

This blueprint will contain device specific functions. Current functions include:

- Repeat the last spoken text to speech from that device
- Set the different modes for the satellite device
- Change views by voice
- Adjust volume by level
- Adjust volume by step
- Mute/Unmute volume
- Stop music playback and return to normal mode
- Pause playback
- Next song
- Adjust music volume by level
- Adjust music volume by step
- Mute/Unmute music

## Suggested Command Translations

### Repeat Command

- en: `(what did you say  | [please] say that again [please] | [please] repeat that [please])`
- de: `(Was hast du gesagt  | [Bitte] sag das noch einmal [bitte] | [Bitte] wiederhole das [bitte])`

### Mode Command

- en: `(set mode [to] {mode} | turn on {mode} mode | set [to] {mode} mode)`
- de: `(setze den Modus [auf] {mode} | schalte {mode} Modus ein | setze [auf] {mode} Modus)`

### View Command

- en: `(set view [to] {view} | change [to] {view} view | set [to] {view} view)`
- de: `(setze [die] Ansicht [auf] {view} | wechsle [zu] {view} Ansicht | setze [auf] {view} Ansicht | Zeige [der|die|das] {view})`

### Do Not Disturb Command

- en: `(set do not disturb [mode] [to] off | turn off do not disturb [mode] | end do not disturb [mode] | cancel do not disturb [mode])`
- de: `(setze den Nicht stören [Modus] [auf] aus | schalte den Nicht stören [Modus] aus | beende den Nicht stören [Modus] | abbreche den Nicht stören [Modus])`

### Set Volume Command

- en: `[set | turn] [the] volume [to] {level}`
- de: `[Setze | Schalte] [die] Lautstärke [auf] {level}`

### Adjust Volume Command

- en: `turn {up_down} [the] volume`
- de: `Schalte [die] Lautstärke {up_down}`

### Mute Volume Command

- en: `mute [the] [volume]`
- de: `Schalte [die] Lautstärke stumm`

### Unmute Volume Command

- en: `unmute [the] [volume]`
- de: `Schalte [die] Lautstärke [wieder] an`

### Stop Music Command

- en: `stop [the] music`
- de: `Stoppe [die] Musik`

## To do

- Add rewind/fast forward XX seconds/minutes, previous/restart track
- query what song/media is playing by voice
- Add 'move to [area]' to move music playback from one satellite to another
- Add device screen reload/refresh

## Changelog

| Version | Description                                                                              |
| ------- | ---------------------------------------------------------------------------------------- |
| v 1.4.0 | Add more music specific functions                                                        |
| v 1.3.0 | Add additional functions pause, next, additional                                         |
| v 1.2.2 | Stop music stops music player device and expires timer to go back to home screen quicker |
| v 1.2.1 | Add volume control and stop music (Thanks @jimmyjamesbob)                                |
| v 1.2.0 | Add view functionality                                                                   |
| v 1.1.0 | Add mode functionality                                                                   |
| v 1.0.0 | Initial release                                                                          |
