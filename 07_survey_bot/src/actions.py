
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction




class SurveyForm(FormAction):
 def name(self):
  return "survey_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["first_reply","rate_quality","innovative","price_service","buy_service","replace_service","rate_service","like_most","improve_service"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "first_reply": [
                self.from_text(),
            ],
            "rate_quality": [
                self.from_text(),
            ],
            
            "innovative": [
                self.from_text(),
            ],
            "price_service": [
                self.from_text(),
            ],
            "buy_service": [
                self.from_text(),
            ],
            "replace_service": [
                self.from_text(),
            ],
            "rate_service": [
                self.from_text(),
            ],
            "like_most": [
                self.from_text(),
            ],
            "improve_service": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Thank you for your patience")    
    return []
