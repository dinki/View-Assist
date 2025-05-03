# List Management
This Home Assistant blueprint, View Assist - List Management, allows users to manage a to-do list using voice commands. 
It supports adding, removing, and displaying items on a specified list. 
The blueprint integrates with Home Assistant's conversation platform and provides customizable phrases for voice interactions.
The blueprint also supports multiple languages (e.g., English, German, French, Spanish) and can display the list on a dashboard if a compatible device is available. 
Some of these translation were done with automatic translation, so feel free to raise a PR to improve the wording.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fviewassist-integrationprep%2FView_Assist_custom_sentences%2FList_Management%2Fblueprint-listmanagement.yaml)

## Example Sentences
- "Add milk to my shopping list."
- "Remove eggs from the grocery list."
- "What's on my shopping list?"
- "Show me the grocery list."

## Reverse list order
Since Home Assistant to-do lists show the newest items at the bottom, you may want to reverse the order of the list.
The closest you can get to this is to use the `reverse_spoken_list` function in the blueprint to reverse the sequence in which items are spoken during requests to show the list.

This will not change the order of the items shown on the dashboard, as this is controlled by the [to-do-list card](https://www.home-assistant.io/dashboards/todo-list/). 
As of Home Assistant 2025.4, the to-do-list card does not support reversing the order of items. An alternative is to use the `display_order` attribute which does not allow sorting based on creation date however.
The closest you can get is to add the following line into the CSS Block of your list view. It will scroll the view to the bottom of the list, so the newest items are shown first.
```css
ha-card {
  background-color: transparent;
  box-shadow: none;
  border: none;
  position: absolute;
  top: 5vh; /* Play with this value to adjust top spacing */
  height: 80vh; /* Limit the vertical size to allow scrolling */
  flex-direction: column-reverse; /* <-- Add this line */
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
}
```

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

## TODO
- [X] Extend View to allow for scrolling
- [ ] Extend View to allow for multiple columns to fit more items