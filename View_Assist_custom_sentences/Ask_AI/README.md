# Ask AI

<a href="https://www.youtube.com/watch?v=2xSvFU5Xlss"><img src="https://img.youtube.com/vi/2xSvFU5Xlss/mqdefault.jpg" width="60%"></a>

Detailed install video:

https://www.youtube.com/watch?v=2xSvFU5Xlss

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FAsk_AI%2Fblueprint-askai.yaml)

An on demand call to OpenAI for answering questions about life, love and happiness.  Seriously though, this allows the user to use LLM to get answers to questions and greatly simplifies the need for coding a lot of these things by hand.  Be warned, though.  LLMs are known to provide bogus answers sometimes so use with caution.

Requirements:
  * Must have a paid OpenAI account.  Don't worry.  The price to use is very low (pennies a month).  See [this video](https://www.youtube.com/watch?v=4D6bIDcVOWc) for more information for pricing and set up
  * [Info View](https://github.com/dinki/View-Assist/wiki/View-Assist-Custom-Views-Gallery#info)

I am using gpt-3.5-turbo which is considerably cheaper than the default gpt-4 model.
*UPDATE* Discord user vash2695 wrote "In case it hasn't been mentioned already, you should set that integration to use "gpt-4o-mini". It's substantially smarter than 3.5 while also being cheaper!"


Usage is 'Ok nabu ask AI [your question]' .

Additionally, user Andrew Steel is reporting that this blueprint will also work with local Ollama AI using [hass-ollama-conversation](https://github.com/ej52/hass-ollama-conversation#options)
