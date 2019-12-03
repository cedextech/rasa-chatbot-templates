from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction
import json

import requests
from dotenv import load_dotenv
from pathlib import Path
import os 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
'''os.getenv() used to read varibles from .env file'''
ticket_url = os.getenv("all_tikcket_url")
apikey=os.getenv("api_key")

def show_all():
  response = requests.get(ticket_url,auth=(apikey, 'X'))
  return response.json()
class AllTickets(Action):
 """example of custom action"""   
 def name(self):
  """name of the custom action"""
  return "action_all_tickets"

 def run(self,dispatcher,tracker,domain):
  """action for display all tickets in freshdesk"""  
  data=show_all()
  leng=len(data)
  for i in range(leng):
   message=str((i+1))+'.'+data[i]['subject']+'\n'+'Created Date:'+data[i]['created_at']
   dispatcher.utter_message(message)	
def CreateTicket(description,subject,email,priority,status):
    """api call for create aticket in freshdesk help desk"""
    headers = {
    'Content-Type': 'application/json',
    }

    data = { "description": description, "subject": subject, "email": email, "priority": priority, "status": status} 
    json_data=json.dumps(data);

    response = requests.post(ticket_url, headers=headers, data=json_data, auth=(apikey, 'X'))

    return response
class createTicketForm(FormAction):
 """Example of a custom form action"""   
 def name(self):
  """Unique identifier of the form"""  
  return "create_ticket_form"

 def required_slots(self,tracker) -> List[Text]:
   """A list of required slots that the form has to fill"""
   return ["description","subject","email","priority","status"]
 def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
    """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""


    return {
            "description": [
                self.from_text(),
            ],
            "subject": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
            "priority": [
                self.from_text(),
            ],
            "status": [
                self.from_text(),
            ],


        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    """Define what the form has to do
            after all required slots are filled"""
    dispatcher.utter_message("Your ticket creation status in freshdesk")    
    return []

class CreatenewTicket(Action):
 """example of custom action"""   
 def name(self):
  """name of the custom action"""
  return "action_create_tickets"    
 def run(self,dispatcher,tracker,domain):
  """action for create ticket in freshdesk"""
  descri=tracker.get_slot("description")
  sub=tracker.get_slot("subject")  
  email=tracker.get_slot("email")
  prio=tracker.get_slot("priority")
  sta=tracker.get_slot("status")
  priority_type=int(prio)
  status_code=int(sta)
  data=CreateTicket(descri,sub,email,priority_type,status_code)
  if(data.status_code==201):
    dispatcher.utter_message('The ticket is sucessfully created in freshdesk')
  else:
    dispatcher.utter_message('Something bad happend while ticket creation')
    
class UpdateTicket(Action):
 """example of custom action"""   
 def name(self):
  """name of the custom action"""
  return "action_update_tickets"    
 def run(self,dispatcher,tracker,domain):
  data=show_all()
  leng=len(data)
  dispatcher.utter_message("Here is your Ticket details")
  for i in range(leng):
    message="Ticket Id:"+str(data[i]['id'])+"\n"+"Ticket Subject:"+data[i]['subject']
    dispatcher.utter_message(message)

class updateTicketForm(FormAction):
 """Example of a custom form action"""   
 def name(self):
  """Unique identifier of the form"""  
  return "update_ticket_form"

 def required_slots(self,tracker) -> List[Text]:
   """A list of required slots that the form has to fill"""
   return ["priority-up","status-up","ticket_id"]
 def slot_mappings(self) -> Dict[Text,Union[Dict, List[Dict]]]:
    """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""


    return {
            "priority-up": [
                self.from_text(),
            ],
            "status-up": [
                self.from_text(),
            ],
            "ticket_id": [
                self.from_text(),
            ],


        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    """Define what the form has to do
            after all required slots are filled"""
    dispatcher.utter_message("Here is the update information")        
    return []
def updateticket(ticket,priority,status):
  """api call for update a tiket in freshdesk"""
  headers = {
    'Content-Type': 'application/json',
  }
  data = { "priority": priority, "status": status }
  json_data=json.dumps(data);
  url=ticket_url+'/'+str(ticket)

  response = requests.put(url, headers=headers, data=json_data, auth=(apikey, 'X'))
  return response

class UpdatedTicket(Action):
 """example of custom action"""   
 def name(self):
  """name of the custom action"""
  return "action_updatedtickets"    
 def run(self,dispatcher,tracker,domain):
  """action for update ticket in freshdesk"""
  tick=tracker.get_slot("ticket_id")
  prio=tracker.get_slot("priority-up")
  sta=tracker.get_slot("status-up")
  priority_type=int(prio)
  status_code=int(sta)
  data=updateticket(tick,priority_type,status_code)
  if(data.status_code==200):
    dispatcher.utter_message('The ticket is sucessfully updated in freshdesk')
  else:
    dispatcher.utter_message('Something bad happend while ticket updation')       
