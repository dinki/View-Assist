# Play Music with Music Assistant

## Requirements

- Music Assistant server installed and integrated with Home Assistant
- View: [Music view](../views/music)
- The recently added musicplayer_device must be added to your View Assistant device configuration as explained in the [Satellite Custom Device Configuration](https://github.com/dinki/View-Assist/wiki/View-Assist-device-configuration#satellite-custom-device-configuration) portion of the wiki. This should be a Music Assistant player device. Typically these will be named the same as your mediaplayer_device but with a \_2 on the end

## Translations

This section provides examples of the custom sentences in different languages.
Adjustments may be needed based on your specific usage and preferences.

### Play Artist Command

- en: `(play the artist {artist} | play some {artist} [music] |play [some] [music | songs] by {artist})`
- de: `(Spiele den Künstler {artist} | Spiele etwas {artist} [Musik] | Spiele [etwas] [Musik | Lieder] von {artist})`

### Play Playlist Command

- en: `start [the] {playlist} playlist`
- de: `Spiele [die] Playlist {playlist}`

### Play Song Command

- en: `play {song} by {artist}`
- de: `Spiele [den Song|den Titel] {song} von {artist}`

### Queue Song Command

- en: `(queue | cue | Q) {song} by {artist}`
- de: `Setze [den Song|den Titel] {song} von {artist} [in|auf] die Warteschlange`

## Changelog

| Version | Description                                                                                  |
| ------- | -------------------------------------------------------------------------------------------- |
| v 1.2.1 | Correct typo in variable name                                                                |
| v 1.2.0 | Various improvements                                                                         |
| v 1.0.4 | Add additional sentences, improvements and conditional responses                             |
| v 1.0.3 | Add new MA instance requirement to BP inputs                                                 |
| v 1.0.2 | Change action calls to use new music_assistant viariant                                      |
| v 1.0.1 | Move change view to beginning of sequences and change default view values to the correct one |
| v 1.0.0 | Initial release                                                                              |
