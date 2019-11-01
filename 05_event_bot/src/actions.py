from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action

class VenueConfrence(Action):
 def name(self):
  """name of the custom action"""
  return "action_venu_confrence_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Batman Room",
                            "subtitle": "Batman Room - ABC Road,Kochi.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/batman_room_confrence",
                                    "title": "View Session"
                                },
                                
                            ]
                        },
                        {
                            "title": "Superman Room",
                            "subtitle": "Superman Room - XYZ Road,Kochi",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/superman_room_confrence",
                                    "title": "View Session"
                                },
                            ]
                        },
                        {
                            "title": "Hero Room",
                            "subtitle": "Superman Room - XYZ Road,Kochi",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "hero_room_confrence",
                                    "title": "View Session"
                                },
                            ]
                        },
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class BatmanRoomDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_batman_rooom_details"

 def run(self,dispatcher,tracker,domain):  
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Build  a chatbot with Dialogflow",
                            "subtitle": "How to build a chatbot with Dialogflow within 15 miniutes.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot with AWS Lex",
                            "subtitle": "Quick demo how to use chatbot with AWS Lex",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class SupermanRoomDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_superman_rooom_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Chatbot in 2018",
                            "subtitle": "Chatbot trend in 2018",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Dialogflow for beginner",
                            "subtitle": "This is a quick introduction to Dialogflow",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot with AWS Lex",
                            "subtitle": "Quick demo how to use chatbot with AWS Lex",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []      
class HeroRoomDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_hero_rooom_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Build  a chatbot with Dialogflow",
                            "subtitle": "How to build a chatbot with Dialogflow within 15 miniutes.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot in 2018",
                            "subtitle": "Chatbot trend in 2018",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Dialogflow for beginner",
                            "subtitle": "This is a quick introduction to Dialogflow",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class SpeakerConfrence(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_confrence_details"

 def run(self,dispatcher,tracker,domain):	
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Andrew King",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Chatbot expert. Andrew has been developing chatbot since 2015.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_session_speaker1",
                                    "title": "View Session"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/session_speaker3",
                                    "title": "Show More"
                                },

                                
                            ]
                        },
                        {
                            "title": "Daniel Evanas",
                            "image_url":"https://media.nature.com/w300/magazine-assets/d41586-018-07881-1/d41586-018-07881-1_16369438.jpg",
                            "subtitle": "Daniel is a world class AI and Chatbot expert",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_session_speaker2",
                                    "title": "View Session"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/session_speaker3",
                                    "title": "Show More"
                                },

                                
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class SpeakeroneDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakerone_details"

 def run(self,dispatcher,tracker,domain): 
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Build  a chatbot with Dialogflow",
                            "subtitle": "How to build a chatbot with Dialogflow within 15 miniutes.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot with AWS Lex",
                            "subtitle": "Quick demo how to use chatbot with AWS Lex",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  
class SpeakertwoDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speakertwo_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Chatbot in 2018",
                            "subtitle": "Chatbot trend in 2018",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Dialogflow for beginner",
                            "subtitle": "This is a quick introduction to Dialogflow",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot with AWS Lex",
                            "subtitle": "Quick demo how to use chatbot with AWS Lex",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return [] 
class SpeakerConfrenceMore(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_confrence_more_details"

 def run(self,dispatcher,tracker,domain): 
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Rose Stone",
                            "image_url": "https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                            "subtitle": "10 year's experience in C.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_rosestone",
                                    "title": "View Session"
                                }, 
                            ]
                        },
                        {
                            "title": "Freya Burke",
                            "image_url": "https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                            "subtitle": "Founder of many suuccessful startups,speaker and investor",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_freyabruke",
                                    "title": "View Session"
                                }      
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return
class SpeakeRoseStoneDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_rosestone_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Chatbot with AWS Lex",
                            "subtitle": "Quick demo how to use chatbot with AWS Lex",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return [] 
class SpeakerFreyaDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_speaker_freya_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Chatbot in 2018",
                            "subtitle": "Chatbot trend in 2018",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Dialogflow for beginner",
                            "subtitle": "This is a quick introduction to Dialogflow",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View Info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return [] 
class SessionConfrenceDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_confrence_details"

 def run(self,dispatcher,tracker,domain):  
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Build  a chatbot with Dialogflow",
                            "subtitle": "How to build a chatbot with Dialogflow within 15 miniutes.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_one_speaker_details",
                                    "title": "View Speakers"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/session_speaker3",
                                    "title": "Show More"
                                },

                                
                            ]
                        },
                        {
                            "title": "Chatbot in 2018",
                            "subtitle": "QChatbot trend in 2018",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_two_speaker",
                                    "title": "View Speakers"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/session_speaker3",
                                    "title": "Show More"
                                },
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  
class SessiononeSpeakerConfrence(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_speaker_confrence_details"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Andrew King",
                            "image_url":"https://www.accenture.com/gb-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Images/Global-3/27/Accenture-Human-Machine-AI-James.png",
                            "subtitle": "Chatbot expert. Andrew has been developing chatbot since 2015.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Daniel Evanas",
                            "image_url":"https://media.nature.com/w300/magazine-assets/d41586-018-07881-1/d41586-018-07881-1_16369438.jpg",
                            "subtitle": "Daniel is a world class AI and Chatbot expert",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class SessiontwoSpeakerConfrence(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_two_speaker_confrence_details"

 def run(self,dispatcher,tracker,domain):  
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Daniel Evanas",
                            "image_url":"https://media.nature.com/w300/magazine-assets/d41586-018-07881-1/d41586-018-07881-1_16369438.jpg",
                            "subtitle": "Daniel is a world class AI and Chatbot expert.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        {
                            "title": "Freya Burke",
                            "image_url": "https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
                            "subtitle": "Founder of many suuccessful startups,speaker and investor",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/view_information",
                                    "title": "View info"
                                },
                                {                                
                                    "type": "postback",
                                    "payload": "/subsctibition_to_update",
                                    "title": "Subscribe to updates"
                                },

                                
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  

class SessionMoreConfrenceDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_session_more_confrence_details"

 def run(self,dispatcher,tracker,domain): 
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Build  a chatbot with Dialogflow",
                            "subtitle": "How to build a chatbot with Dialogflow within 15 miniutes.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/session_one_speaker_details",
                                    "title": "View Speakers"
                                },
                               
                                
                            ]
                        },
                        
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []    
