# Sports View

![](./sportsview.png)

* **Description**: Shows matchup results, in game or upcoming information for various sports events
* **Defaultname**:  sports
* **Current Version**: v1.0.0
* **Code link**:  [Webpage View Raw Code](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/sports/sports.yaml)
* **Special Requirements**: Requires ha-teamtracker-card

## Installation 

This card can be added by copy pasting the raw code into a new view.   The [ha-teamtracker-card](https://github.com/vasqued2/ha-teamtracker-card) must be installed to use this view. This can be installed via HACS.

## Example Sentences
- "How did the Lakers do?"
- "What’s the score of the Yankees game?"
- "How are the Packers doing?"
- "Show me the score of the Barcelona match."
- "What’s the score of the Bruins game?"

## Translations
This section provides examples of the custom sentences in different languages.  
Adjustments may be needed based on your specific usage and preferences.

### English
```yaml
trigger_phrases:
  - how did [the] {team} do
  - (what is | what's) the score of the {team} (game | match)
  - how (is | are) [the] {team} doing
  - how (is | are) [the] {team} (game | match) [going]
```

### German
```yaml
trigger_phrases:
  - Wie hat [das] {team} gespielt
  - (Wie steht es bei | Was ist der Spielstand) [von] [dem] {team} (Spiel | Match)
  - Wie läuft es bei [dem] {team}
  - Wie läuft [das] {team} (Spiel | Match)
```

### Spanish
```yaml
trigger_phrases:
  - Cómo le fue al {team}
  - (Cuál es | Qué es) el marcador del partido de {team}
  - Cómo va el {team}
  - Cómo va el partido de {team}
```

### French
```yaml
trigger_phrases:
  - Comment s'est passé le match de {team}
  - (Quel est | C'est quoi) le score du match de {team}
  - Comment va {team}
  - Comment se passe le match de {team}
```

### Italian
```yaml
trigger_phrases:
  - Come è andata la partita del {team}
  - (Qual è | Che cosa è) il punteggio della partita del {team}
  - Come sta andando il {team}
  - Come sta andando la partita del {team}
```

## Changelog

| Version | Description                                   |
|---------|-----------------------------------------------|
| v 1.3.0 | Added german, spanish and french translations |
| v 1.2.0 | Added italien translation                     |
| v 1.0.0 | Initial release                               |


