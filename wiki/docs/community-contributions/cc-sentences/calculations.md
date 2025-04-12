---
title: Calculations
---

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FCalculations%2Fblueprint-calculations.yaml)

This blueprint allows you to calculate the result of a mathematical expression using Wolfram Alpha's Short Answers API. The spoken response includes both the expression and the answer, in order to confirm the user was accurately understood. This is a community contribution authored by user [michelle-avery (Github)](https://github.com/michelle-avery)/miniconfig (Discord). Support can be obtained through the View Assist [Discord server](https://discord.com/channels/1241796965344481440/1295408431498395709) or the [discussion group](https://github.com/dinki/View-Assist/discussions) on Github. Please tag the author in your message.

## Prerequisites

- You must have Pyscript installed [See installation video](https://www.youtube.com/watch?v=jpJxZaisbGQ)
- You must set up an account and create an API key for Wolfram Alpha's [Short Answers](https://products.wolframalpha.com/short-answers-api/documentation) API. Free API keys are alloted 2,000 calls per month.
- You must download the [required pyscript](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FAsk_Wolfram%2Fviewassist-get_wolfram_short_answer.py), add your appid to the `appid` parameter, and place this file in your 'pyscripts' directory on your Home Assistant Server. Note that if you have multiple custom sentences using this script, this only needs to be performed once.

## Changelog

| Version | Description     |
| ------- | --------------- |
| v 1.0.0 | Initial release |
