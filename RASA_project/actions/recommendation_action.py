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

            age = tracker.get_slot("age")
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

            # if age == None:
            #     prompt = gpt3_prompt()
            #     dispatcher.utter_message(text = prompt.get_question("age"))
            if gender == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("It's for a male"))
            
            if size == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("I need them in L size"))

            elif color == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("yes, show me something in brown or grey"))

            elif clothes == None:
                prompt = gpt3_prompt()
                dispatcher.utter_message(text = prompt.get_question("I want to buy jeans")) 
            else:
                if gender in ['man','father','dad','daddy','boy','uncle','husband','grandfather','grandson']:
                    gender = "male"
                elif gender in ['woman','mother','mom','mommy','aunt','wife','grandmother','granddaughter']:
                    gender = "female"
                else:
                    gender = "other"

                query ="Gender == @gender and Size == @size and Color in @color and Product_type == @clothes"
                print(query)
                first_search_result = df.query(query)
                print(first_search_result)
                recommendation = first_search_result["ITEM"].to_list()
                print(recommendation)
                for item in recommendation[:5]:
                    dispatcher.utter_message(image = item)
                
            return []