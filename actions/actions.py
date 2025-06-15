# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionGetWeather(Action):

    def name(self) -> str:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict):

        city = tracker.get_slot("city")
        if not city:
            dispatcher.utter_message(text="Я не понял город. Повтори, пожалуйста.")
            return []

        try:
            response = requests.get(f"https://wttr.in/{city}?format=3")
            if response.status_code == 200:
                dispatcher.utter_message(text=response.text)
            else:
                dispatcher.utter_message(text=f"Не удалось получить погоду для города {city}.")
        except Exception as e:
            dispatcher.utter_message(text=f"Произошла ошибка: {str(e)}")

        return []
