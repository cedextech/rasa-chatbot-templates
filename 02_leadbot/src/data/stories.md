## begin conversation
* greet
  - utter_greet
  - utter_menu

## combined begin with url
* greet
    - utter_greet
    - utter_menu
* begin_lead
    - utter_lead_q1
    - lead_form_p1
    - form{"name": "lead_form_p1"}
    - form{"name": null}
* accept
    - lead_form_p2
    - form{"name": "lead_form_p2"}
    - form{"name": null}
    - lead_form_p3
    - form{"name": "lead_form_p3"}
    - form{"name": null}
    - utter_lead_q3
    - utter_lead_q4
    - utter_lead_q5

## combined begin without url
* greet
    - utter_greet
    - utter_menu
* begin_lead
    - utter_lead_q1
    - lead_form_p1
    - form{"name": "lead_form_p1"}
    - form{"name": null}
* reject
    - lead_form_p3
    - form{"name": "lead_form_p3"}
    - form{"name": null}
    - utter_lead_q3
    - utter_lead_q4
    - utter_lead_q5