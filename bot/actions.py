from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import rasa_sdk

sabores = ["calabresa", "catupiri", "chocolate", "frango"]

class ActionCheckPizzaFlavor(Action):
	def name(self):
		return "action_pizza_flavors"
		
	def run(self, dispatcher, tracker, domain):
		message = "Nós temos os seguintes sabores:\n"
		for sabor in sabores:
			message += "() {sabor}\n".format(sabor=sabor)
		dispatcher.utter_message(message)
		return []
		

class CheckPizzaFlavor(Action):
	def name(self):
		return "action_check_flavor"
		
	def run(self, dispatcher, tracker, domain):
		flavor = str(tracker.get_slot('sabor'))
		flavor = flavor.lower()
		
		if flavor not in sabores:
			dispatcher.utter_message('nao possuimos este sabor')
			return [rasa_sdk.events.FollowupAction("action_listen")]
		
		dispatcher.utter_message('uma pizza de {sabor} registrada!'.format(sabor=flavor))
		return [SlotSet('sabor', flavor)]

class CheckPayment(Action):
    def name(self):
        return "action_check_payment"

    def run(self, dispatcher, tracker, domain):
        payment = str(tracker.get_slot('pagamento'))

        dispatcher.utter_message('Ok, pagamento será realizado no {pagamento}!'.format(pagamento=payment))
        return [SlotSet('sabor', None)]
