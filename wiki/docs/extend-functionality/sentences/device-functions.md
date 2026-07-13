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
- it: `(cosa hai detto | puoi ripetere | ripeti [per favore])`

### Mode Command

- en: `(set mode [to] {mode} | turn on {mode} mode | set [to] {mode} mode)`
- de: `(setze den Modus [auf] {mode} | schalte {mode} Modus ein | setze [auf] {mode} Modus)`
- it: `(metti | attiva | imposta) [la] modalità {mode}`

### View Command

- en: `(set view [to] {view} | change [to] {view} view | set [to] {view} view)`
- de: `(setze [die] Ansicht [auf] {view} | wechsle [zu] {view} Ansicht | setze [auf] {view} Ansicht | Zeige [der|die|das] {view})`
- it: `(vai alla vista {view} | mostra [la vista] {view} | metti la vista {view})`

### Do Not Disturb Command

- en: `(set do not disturb [mode] [to] off | turn off do not disturb [mode] | end do not disturb [mode] | cancel do not disturb [mode])`
- de: `(setze den Nicht stören [Modus] [auf] aus | schalte den Nicht stören [Modus] aus | beende den Nicht stören [Modus] | abbreche den Nicht stören [Modus])`
- it: `(togli | disattiva | spegni) [la modalità] non disturbare`

### Set Volume Command

- en: `[set | turn] [the] volume [to] {level}`
- de: `[Setze | Schalte] [die] Lautstärke [auf] {level}`
- it: `[metti | imposta] [il] volume (a | al) {level}`

### Volume Up Command

- en: `turn up [the] volume`
- de: `Schalte [die] Lautstärke lauter`
- it: `(alza | aumenta) il volume`

### Volume Down Command

- en: `turn down [the] volume`
- de: `Schalte [die] Lautstärke leiser`
- it: `(abbassa | diminuisci) il volume`

### Mute Volume Command

- en: `mute [the] [volume]`
- de: `Schalte [die] Lautstärke stumm`
- it: `(metti muto | muto | zitto | silenzio)`

### Unmute Volume Command

- en: `unmute [the] [volume]`
- de: `Schalte [die] Lautstärke [wieder] an`
- it: `(togli il muto | riattiva l'audio | rimetti l'audio)`

### Stop Music Command

- en: `stop [the] music`
- de: `Stoppe [die] Musik`
- it: `((ferma | stoppa | spegni) la musica | basta musica)`

## Changelog

| Version | Description                                                                              |
| ------- | ---------------------------------------------------------------------------------------- |
| v 1.5.0 | Split Adjust Volume into Volume Up/Down commands so translated phrases work; fix missing German response strings |
| v 1.4.7 | Add Italian translation                                                                  |
| v 1.4.6 | Added translations                                                                       |
| v 1.4.5 | Add Serbian translations                                                                 |
| v 1.4.4 | Explicitly set path for setting view                                                     |
| v 1.4.3 | Add Dutch translation                                                                    |
| v 1.4.2 | Add Polish translation                                                                   |
| v 1.4.1 | Add 'what song is playing'. Thanks Rymez2k                                               |
| v 1.4.0 | Add more music specific functions                                                        |
| v 1.3.0 | Add additional functions pause, next, additional                                         |
| v 1.2.2 | Stop music stops music player device and expires timer to go back to home screen quicker |
| v 1.2.1 | Add volume control and stop music (Thanks @jimmyjamesbob)                                |
| v 1.2.0 | Add view functionality                                                                   |
| v 1.1.0 | Add mode functionality                                                                   |
| v 1.0.0 | Initial release                                                                          |
