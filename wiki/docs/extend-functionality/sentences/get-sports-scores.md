# Get Sports Scores

[![Image](https://img.youtube.com/vi/Dv7Z_xJk6Ug/mqdefault.jpg)](https://www.youtube.com/watch?v=Dv7Z_xJk6Ug)

Detailed install video:
https://www.youtube.com/watch?v=Dv7Z_xJk6Ug

Note that this video was recorded before the integration existed so you can skip the blueprint and view install as those are now automatically provided for you

This blueprint allows the user to make a voice request for sports scores using the fantastic Team Tracker extension. The users asks for the team by using the team mascot
name. Some teams like the Rangers and Cardinals have multiple teams using those mascots. User will need to specify the city and mascot for these. This can be changed in code
if desired to make things easier. View Assist devices with displays will also get a fantastic display via the Team Tracker card. Leagues supported are NFL, MLB, NBA, WNBA, NHL and MLS. Individual college team support is planned for a future update.

Requirements:

- [Team Tracker extension](https://github.com/vasqued2/ha-teamtracker) v0.1.4.1 must be installed. This can be installed with HACS
- [Team Tracker Card](https://github.com/vasqued2/ha-teamtracker-card). This can be installed with HACS
- A Team Tracker sensor device created using the UI (not YAML). Suggested name 'team_tracker'. I configured mine as NFL and team 'NO'. It doesn't matter though. Any valid NFL team is fine (Who Dat!).
- View Assist [sports view](../views/sports) using provided YAML (will link when released). Suggested name 'sports'

Thanks to vasqued2 for the great work on Team Tracker and Mr. Picc010 for his help with the voice response logic

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

## To do

- Plural state not working properly
- Add more queries for things like next game

## Changelog

| Version | Description                |
| ------- | -------------------------- |
| v 1.3.1 | Bug fix for college sports |
| v 1.3.0 | Rework                     |
| v 1.0.0 | Initial release            |
