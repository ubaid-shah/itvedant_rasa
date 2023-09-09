# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "course_fees_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course_n=next(tracker.get_latest_entity_values("course_name"),None)

        if "the python developer" in course_n:
            dispatcher.utter_message(text="The fees of the python developer course is Rs.20000")
        elif "the SQL developer" in course_n:
            dispatcher.utter_message(text="The fees of the SQL developer course is Rs.25000")
        elif "the Full Stack developer" in course_n:
            dispatcher.utter_message(text="The fees of the Full Stack developer is Rs.15000")

        return []
