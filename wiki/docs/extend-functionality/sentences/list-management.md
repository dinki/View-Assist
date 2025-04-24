# List Management

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Fmain%2FView_Assist_custom_sentences%2FList_Management%2Fblueprint-listmanagement.yaml)

[![Image](https://img.youtube.com/vi/h6WmQ7LiO_0/mqdefault.jpg)](https://www.youtube.com/watch?v=h6WmQ7LiO_0)

Detailed install video: https://youtu.be/h6WmQ7LiO_0

Required View: [list view](../views/list)

Allows user to add and remove items from a shopping list.  User can also request to show the shopping list and it will be displayed on View Assist satellite devices with displays.



Special thanks to Elwing for her work on this automation and view

## Example Sentences
- "Add milk to my shopping list."
- "Remove eggs from the grocery list."
- "What's on my shopping list?"
- "Show me the grocery list."

## Translations
This section gives some examples of how to use the custom sentences in different languages. The translations are not perfect and may need to be adjusted based on your specific use case.

### English
```yaml
command_add1: >-
  (add|at) {item} to [my | the][grocery|shopping] list
command_remove1: >-
  remove {item} from [my | the][grocery|shopping] list
command_remove2: take {item} off [my | the] [grocery|shopping] list
command_show1: >-
  (what's | what is) on [my| the] [grocery|shopping] list
command_show2: show [me] [my| the] [grocery|shopping] list
```

### German
```yaml
command_add1: >-
  (Füge | Setze) {item} [auf] [meine | die | meiner]
  [Einkaufs|Einkaufsliste| Einkaufliste] [hinzu]
command_remove1: >-
  (Entferne | Lösche | Nehme) {item} von [meiner | der]
  [Einkaufs|Einkaufsliste| Einkaufliste]
command_remove2: (Nimm) {item} von [meiner | der] [Einkaufs|Einkaufsliste| Einkaufliste]
command_show1: >-
  (Was steht | Was ist) auf [meiner | der] [Einkaufs|Einkaufsliste|
  Einkaufliste]
command_show2: (Zeig [mir]) [meine | die] [Einkaufs|Einkaufsliste| Einkaufliste]
```

### Spanish
```yaml
command_add1: >-
  (añade | agrega) {item} a [mi | la][lista de compras | lista de la compra]
command_remove1: >-
  (elimina | quita) {item} de [mi | la][lista de compras | lista de la compra]
command_remove2: >-
  (saca) {item} de [mi | la][lista de compras | lista de la compra]
command_show1: >-
  (¿qué hay | qué está) en [mi | la][lista de compras | lista de la compra]?
command_show2: >-
  (muestra [me]) [mi | la][lista de compras | lista de la compra]
```

### French
```yaml
command_add1: >-
  (ajoute | ajoutez) {item} à [ma | la][liste de courses | liste d'achats]
command_remove1: >-
  (retire | enlève) {item} de [ma | la][liste de courses | liste d'achats]
command_remove2: >-
  (enlève) {item} de [ma | la][liste de courses | liste d'achats]
command_show1: >-
  (qu'est-ce qu'il y a | qu'est-ce qui est) sur [ma | la][liste de courses | liste d'achats] ?
command_show2: >-
  (montre [moi]) [ma | la][liste de courses | liste d'achats]
```

## Changelog

| Version | Description |
| ------- | ----------- |
| v 1.2.0 | Added german, spanish and french translations and new options to fine tune spoken content |
| v 1.1.2 | Add entity to VA config for all calls to ensure no errors show when not set |
| v 1.1.1 | Move list view variable out of dictionary |
| v 1.1.0 | Added function |
| v 1.0.0 | Initial release |
