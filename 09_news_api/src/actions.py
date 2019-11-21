from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction

import requests
from dotenv import load_dotenv
from pathlib import Path
import os 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
urlcountry = os.getenv("url")
apikey=os.getenv("apiKey")
urlsource=os.getenv("urlsources")
urltop=os.getenv("urltopic")




def newsapi(country):
	urlnews=urlcountry
	url=urlnews+country
	urlapi=url+'&'+'apiKey='
	urlcoun=urlapi+apikey
	response=requests.get(urlcoun)
	data=response.json()
	return data


def sourcenews(source):
	urlnews=urlsource
	url=urlnews+source
	urlapi=url+'&'+'apiKey='
	urlsour=urlapi+apikey
	response=requests.get(urlsour)
	data=response.json()
	return data

def topicnews(topic):
    urlnews=urltop
    url=urlnews+topic
    urlapi=url+'&'+'apiKey='
    urlcoun=urlapi+apikey
    response=requests.get(urlcoun)
    data=response.json()
    return data




class NewsBBc(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_bbc"

 def run(self,dispatcher,tracker,domain):
  data=sourcenews("bbc-news")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  

class NewsABC(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_abc"

 def run(self,dispatcher,tracker,domain):
  data=sourcenews("abc-news")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  


class NewsABC(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_cnn"

 def run(self,dispatcher,tracker,domain):
  data=sourcenews("cnn")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  
class newsHeadlineus(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_headline_us"

 def run(self,dispatcher,tracker,domain):
  data=newsapi("us")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }  
    dispatcher.utter_custom_json(gt)
  return []
class NewsheadlineIndia(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_headline_india"

 def run(self,dispatcher,tracker,domain):
  data=newsapi("in")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        } 
    dispatcher.utter_custom_json(gt)
  return []

class NewsHeadlineAustralia(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_headline_au"

 def run(self,dispatcher,tracker,domain):
  data=newsapi("au")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        } 
    dispatcher.utter_custom_json(gt)
  return []
class SearchForm(FormAction):
 def name(self):
  return "search_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["topic"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "topic": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("here is related news")    
    return []

class NewsTopic(Action):
 def name(self):
  """name of the custom action"""
  return "action_news_search"

 def run(self,dispatcher,tracker,domain):
  topics=tracker.get_slot("topic")  
  data=topicnews(topics)
  leng=len(data)
  for i in range(leng): 
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []      