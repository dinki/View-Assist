# Get Sports Scores
This Home Assistant blueprint, **View Assist – Get Sports Scores**, allows users to retrieve sports scores for their favorite teams using voice commands.  
It integrates with Home Assistant’s conversation platform and provides customizable sentences for seamless voice interactions.  
The blueprint supports multiple sports leagues (e.g., NFL, NBA, MLB, NHL, MLS, WNBA, and college sports) and multiple languages (e.g., English, German, French, Spanish, Italian).  
Some translations were automatically generated and may benefit from refinement — feel free to submit a PR for improvements!

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fviewassist-integrationprep%2FView_Assist_custom_sentences%2FGet_Sports_Scores%2Fblueprint-getsportsscores.yaml)

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
