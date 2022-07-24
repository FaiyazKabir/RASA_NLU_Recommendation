from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from text_generation import gpt3_prompt

class take_info_and_recommend(Action):

    def name(self) -> Text:
        return "take_info_and_recommend"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

            age = tracker.get_slot("age")
            size = tracker.get_slot("size")
            gender = tracker.get_slot("gender")
            color = tracker.get_slot("color")
            clothes = tracker.get_slot("clothes")
            
            print(age)
            print(size)
            print(gender)
            print(color)
            print(clothes)

            # if age == None:
            #     prompt = gpt3_prompt()
            #     dispatcher.utter_message(text = prompt.get_question("age"))
            
            if size == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("size"))

            elif gender == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("gender"))

            elif color == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("color"))

            elif clothes == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("clothing_pref")) 
            else:
                dispatcher.utter_message(text = "Providing you with a recommendation please wait")
                
            return []