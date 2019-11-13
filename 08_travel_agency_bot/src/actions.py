from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction




class TripplanForm(FormAction):
 def name(self):
  return "trip_plan_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["travel_date","travel_period","trip_type","adults","child","budget","email","phno"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "travel_date": [
                self.from_text(),
            ],
            "travel_period": [
                self.from_text(),
            ],
            
            "trip_type": [
                self.from_text(),
            ],
            "adults": [
                self.from_text(),
            ],
            "child": [
                self.from_text(),
            ],
            "budget": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("❤️❤️❤️Thank you so much for showing your intrest in traveling with us")    
    return []

class ActivitiesOffered(Action):
 def name(self):
  """name of the custom action"""
  return "action_activities_offerd"

 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Zipline Tour",
                            "image_url":"http://teatownkerala.com/wp-content/uploads/2018/03/WNDZIPLINE3.png",
                            "subtitle": "A canopy tour (sometimes called a zip-line tour) provides a route through a wooded and often mountainous landscape making primary use of zip-lines and aerial bridges between platforms built in trees.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/more_info_zipline_tour",
                                    "title": "📄 More Information"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/tour_details_zipline",
                                    "title": "🔍 Tour Details"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/add_to_mytrip",
                                    "title": "✔️ Add to my trip"
                                },

                                
                            ]
                        },
                        {
                            "title": "Natural Exploration",
                            "image_url":"https://media-cdn.tripadvisor.com/media/attractions-splice-spp-540x360/07/6f/41/76.jpg",
                            "subtitle": "A true paradise for those searching for jungles with feantastic beach",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/more_info_natural_exploration",
                                    "title": "📄 More Information"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/tour_details_natural_exploration",
                                    "title": "🔍 Tour Details"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/add_to_mytrip",
                                    "title": "✔️ Add to my trip"
                                },

                                
                            ]
                        },
                        {
                            "title": "Subwing Costa Rica",
                            "image_url":"https://siquijor-island.com/wp-content/uploads/2016/05/13112975_10209553223846197_5242194890031217041_o-702x336.jpg",
                            "subtitle": "Enjoy doing the subwing our main feature",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/more_info_subwing",
                                    "title": "📄 More Information"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/tour_details_subwing",
                                    "title": "🔍 Tour Details"
                                },
                                                                {
                                    "type": "postback",
                                    "payload": "/add_to_mytrip",
                                    "title": "✔️ Add to my trip"
                                },

                                
                            ]
                        },
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []
class testimonials(Action):
 def name(self):
  """name of the custom action"""
  return "action_testimonials"  
 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Daniel⭐⭐⭐⭐⭐",
                            "image_url":"https://devilonwheels.com/wp-content/uploads/2016/01/Zanskar-Changthang-615-2.jpg",
                            "subtitle": "Great team,  safety was never an issue even with rainy tough condition ",
                            
                        },
                        {
                            "title": "Sophie⭐⭐⭐⭐⭐",
                            "image_url":"https://amp.businessinsider.com/images/5b32aa651ae6623f008b492e-750-500.jpg",
                            "subtitle": "Appreciate your encouragement and patience at various times. never forget",
                            
                        },

                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  
class AboutCostaRica(Action):
 def name(self):
  """name of the custom action"""
  return "action_about_costa_rica"  
 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Widely recognized as the world's foremost",
                            "image_url":"https://www.nationalgeographic.com/content/dam/travel/Guide-Pages/north-america/caribbean/costa-rica/costa-rica-travel.adapt.1900.1.jpg",
                            
                        },
                        {
                            "title": "ecotourism destination Costa Rica is small",
                            "image_url":"https://www.euromoney.com/v-fde9e1a6c163377d323d3801f726e2fe/Media/images/euromoney/magazine/oct-19-1/costa%20rica%20sloth%20780.jpg",
                            
                        },
                                                {
                            "title": "but beautiful country with truly dramatic",
                            "image_url":"https://www.maupintravel.com/blog/wp-content/uploads/2019/03/gardens-costa-rica-arenal-volcano-in-costa-rica-hero.jpg",
                            
                        },


                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  
class OtherActivitiesCostRica(Action):
 def name(self):
  """name of the custom action"""
  return "action_otherActivities_costa_rica"  
 def run(self,dispatcher,tracker,domain):
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Bioluminescent Water",
                            "image_url":"http://www.thetraveltwo.com/wp-content/uploads/2017/10/Photo-09-10-2017-22-44-30.jpg",
                            "subtitle":"On the entire planet there are five locations to see vibrant bioluminescent water, of those Costa Rica’s Bahia Beach is number one."
                        },
                        {
                            "title": "Go paragliding",
                            "image_url":"http://www.thetraveltwo.com/wp-content/uploads/2017/10/Photo-14-10-2017-15-50-06.jpg",
                            "subtitle":"Arguably one of the most beautiful places in the world to throw yourself off the side of a mountain to fly like a bird? We twisted and spin 2500ft over Dominical rainforest and beach eye to eye with hawks."
                        },
                                                {
                            "title": "Visit rio celeste",
                            "image_url":"http://www.thetraveltwo.com/wp-content/uploads/2017/10/Photo-03-10-2017-11-44-01.jpg",
                            "subtitle":"Waterfalls, hot springs and the most delicious turquoise water you’ll ever lay your eyes on! The source of this river’s distinctive colour is not a due to chemicals or manipulation but to a physical phenomenon known as Mie scattering."
                        },


                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  
