# Rasa Chatbot Templates

This repository contains a collection of boilerplate templates for different chatbot usecases on RASA platform.

### How to use it?
Here are the simple steps that you can follow to use a template:
* Install RASA https://rasa.com/docs/rasa-x/installation-and-setup/ 
* Create a `project_directory` for your project
* initialize RASA within your `project_directory` by running command `rasa init` 
* Replace the files in the `project_directory` with the ones from downloaded template
* Train the bot with command `rasa train`
* Evaluate the bot in terminal with command `rasa test`
* Start talking to the bot in terminal with command `rasa shell` 

### Important
Being boilerplates, the bots does contain minimal training data for `stories` just enough to structure the conversation skeleton. Please don't forget to improve the conversations with `rasa interactive` command.
