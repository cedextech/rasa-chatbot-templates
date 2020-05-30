# Rasa Chatbot Templates

<p align="center"><img src="https://i.ibb.co/R0Gz8SY/Rasa-Chatbot-Templates.png"></p>

### Introduction
A collection of boilerplate templates for different chatbot usecases on RASA platform.

### Installation & Configuration
Here are the simple steps that you can follow to use a template:
* Install RASA https://rasa.com/docs/rasa-x/installation-and-setup/ 
* Create a `project_directory` for your project
* initialize RASA within your `project_directory` by running command `rasa init` 
* Replace the files in the `project_directory` with the ones from downloaded template
* Train the bot with command `rasa train`
* Evaluate the bot in terminal with command `rasa test`
* OPTIONAL: If you find a file called `actions.py` in your template directory, run this command in a new terminal `rasa run actions`
* Start talking to the bot in terminal with command `rasa shell`

### Important
Being boilerplates, the bots does contain minimal training data for `stories` just enough to structure the conversation skeleton. Please don't forget to improve the conversations with `rasa interactive` command.

### Templates
- **[Smalltalk](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/01_smalltalk_bot)**
- **[Lead Generation](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/02_lead_bot)**
- **[Real Estate](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/03_real_estate_bot)**
- **[Feedback Collection](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/04_feedback_bot)**
- **[Event Concierge](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/05_event_bot)**
- **[Hotel](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/06_hotel_bot)**
- **[Survey](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/07_survey_bot)**
- **[Travel Agency](https://github.com/cedextech/Rasa-Chatbot-Templates/tree/master/08_travel_agency_bot)**
- **[News with API](https://github.com/cedextech/rasa-chatbot-templates/tree/master/09_news_api)**
- **[Freshdesk API for Customer Support](https://github.com/cedextech/rasa-chatbot-templates/tree/master/10_freshdesk_customer_support_bot)**

### Maintainers
[@devkiran](https://github.com/devkiran).
[@freakeinstein](https://github.com/freakeinstein).
[@nileenashaju](https://github.com/nileenashaju)

### Contributing
Feel free to dive in! Open an issue or submit PRs.
