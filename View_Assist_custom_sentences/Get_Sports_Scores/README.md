# Get Sports Scores

<a href="https://www.youtube.com/watch?v=Dv7Z_xJk6Ug"><img src="https://img.youtube.com/vi/Dv7Z_xJk6Ug/mqdefault.jpg" width="60%"></a>

Detailed install video:
https://www.youtube.com/watch?v=Dv7Z_xJk6Ug



[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FGet_Sports_Scores%2Fblueprint-getsportsscores.yaml)


This blueprint allows the user to make a voice request for sports scores using the fantastic Team Tracker extension.  The users asks for the team by using the team mascot
name.  Some teams like the Rangers and Cardinals have multiple teams using those mascots.  User will need to specify the city and mascot for these.  This can be changed in code
if desired to make things easier.  View Assist devices with displays will also get a fantastic display via the Team Tracker card.  Leagues supported are NFL, MLB, NBA, WNBA, NHL and MLS.  Individual college team support is planned for a future update.


Requirements:
  * [Team Tracker extension](https://github.com/vasqued2/ha-teamtracker) v0.1.4.1 must be installed.  This can be installed with HACS
  * [Team Tracker Card](https://github.com/vasqued2/ha-teamtracker-card).  This can be installed with HACS
  * A Team Tracker sensor device created using the UI (not YAML).  Suggested name 'team_tracker'.  I configured mine as NFL and team 'NO'.  It doesn't matter though.  Any valid NFL team is fine (Who Dat!).
  * View Assist [sports view](https://raw.githubusercontent.com/dinki/View-Assist/main/View%20Assist%20dashboard%20and%20views/views/sports/sports.yaml) using provided YAML (will link when released).  Suggested name 'sports'


Thanks to vasqued2 for the great work on Team Tracker and Mr. Picc010 for his help with the voice response logic


## Changelog

v 1.1.0 Add US college sports

v 1.0.0 Initial release

