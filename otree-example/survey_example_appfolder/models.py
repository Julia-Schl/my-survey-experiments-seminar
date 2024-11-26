from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Julia Schleißheimer'
doc = 'Assignment 3'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    name_question = models.StringField(
        label= "<b>What is your name?</b>")
    age_question = models.IntegerField(
        label= "<b>What is your age?</b>", # allow just adults 
        min=18, 
        max=100
    )
    gender = models.IntegerField(initial=-999) 

    academic_level =models.IntegerField(initial=-999) 
    
    study_question = models.StringField(
        label= "<b>What is your study programm?</b> <br>(Please enter the full name in English.)")

    #PopoutPage
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
                        