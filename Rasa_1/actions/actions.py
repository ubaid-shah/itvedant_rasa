# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

courses=['Data Science','Full Stack Development', 'Java Developer Program','Data Analytics']
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "fees_enquiry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        course_n=next(tracker.get_latest_entity_values("course_name"),None)
        # course_n =tracker.latest_message.get('entities')[0].get("value")
        

        if "Data Science" in course_n:
            dispatcher.utter_message(text="The fees of Data Science Course is Rs. 1,60,000")
        elif "Full Stack Development" in course_n:
            dispatcher.utter_message(text="The fees of Full Stack Development Course is Rs. 1,50,000")
        elif "Java Developer" in course_n:
            dispatcher.utter_message(text="The fees of Java Developer Program is Rs. 1,00,000")
        elif "Data Analytics" in course_n:
            dispatcher.utter_message(text="The fees of Data Analytics course is Rs. 50,000")
        else:
            dispatcher.utter_message(text="We do not provide training for this course")
            

        return []
