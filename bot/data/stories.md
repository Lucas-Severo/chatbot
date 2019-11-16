## greet
* greet
 - utter_ask_help

## bye
* bye
 - utter_bye

## goodnight
* night
 - utter_ask_help

## goodmorning
* morning
 - utter_ask_help

## ask_pizza2
* night
 - utter_ask_help
* ask_pizza
 - action_pizza_flavors
* sabor_pizza{"sabor": "abacaxi"}
 - action_check_flavor
 - slot{"sabor": "None"}

## ask_pizza2
* morning
 - utter_ask_help
* ask_pizza
 - action_pizza_flavors
* sabor_pizza{"sabor": "calabresa"}
 - action_check_flavor
 - slot{"sabor": "calabresa"}
 - utter_ask_payment
* payment
 - action_check_payment
 - slot{"sabor": "None"}
* bye
 - utter_bye

## ask_pizza3
* greet
 - utter_ask_help
* sabor_pizza{"sabor": "atum"}
 - action_check_flavor
 - slot{"sabor": "None"}

## ask_pizza4
* sabor_pizza{"sabor": "frango"}
 - action_check_flavor
 - slot{"sabor": "frango"}
 - utter_ask_payment
* payment
 - action_check_payment
 - slot{"sabor": "None"}
* bye
 - utter_bye
