from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from text_generation import gpt3_prompt
import pandas as pd

class take_info_and_recommend(Action):

    def name(self) -> Text:
        return "take_info_and_recommend"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

            age = tracker.get_slot("number")
            size = tracker.get_slot("size")
            gender = tracker.get_slot("gender")
            color = tracker.get_slot("color")
            clothes = tracker.get_slot("clothing_pref")
            
            print(age)
            print(size)
            print(gender)
            print(color)
            print(clothes)

            df = pd.read_csv("D:/RASA_NLU_Recommendation-main-20220724T203213Z-001/RASA_NLU_Recommendation-main/RASA_project/actions/mmd_custom_dataset_by_scribe.csv")

            if age == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("Only 30 years old"))
            elif gender == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("It's for a male"))
            
            elif size == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("I need them in L size"))

            elif color == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("yes, show me something in brown or grey"))

            elif clothes == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("I want to buy jeans")) 
            else:
                if age<12:
                    age = "child"
                else:
                    age = "adult"

                if gender in ['male','man','father','dad','daddy','boy','uncle','husband','grandfather','grandson']:
                    gender = "male"
                    if age == "child":
                        gender="boy"
                elif gender in ['female','woman','mother','mom','mommy','aunt','wife','grandmother','granddaughter']:
                    gender = "female"
                    
                    if age == "child":
                        gender="girl"
                else:
                    gender = "other"

                query ="Age == @age and Gender == @gender and Size == @size and Color in @color and Product_type == @clothes"
                print(query)
                first_search_result = df.query(query)
                print(first_search_result)
                recommendation = first_search_result["ITEM"].to_list()
                print(recommendation)
                if len(recommendation)>0:
                    for item in recommendation[:5]:
                        dispatcher.utter_message(image = item)
                else:
                    dispatcher.utter_message(text = "We do not have any items fitting your requirements")
            return []

class greet_customer(Action):

    def name(self) -> Text:
        return "greet_customer"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
                dispatcher.utter_message(text = "Hi! How can I help you?")
