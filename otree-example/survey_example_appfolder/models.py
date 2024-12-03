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

#this is where we would import andy extra functions or packages we need from python
import random 

#we could also have a python script with custom functions in another file that we can import
from survey_example_appfolder.HelperFunctions import random_number


author = 'Julia Schleißheimer'
doc = 'Assignment 4'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        '''this is a function by otree (same can not be changed)
        which is creating a new subsession. Any variables that are needed to be custom
        (so declaring it in a different way before) are created here'''
        for p in self.get_players():
            #here we want to declare the players to different groups (2 in total)
            #we use a python function here from 'random' we imported earlier
            p.group_assignment = random.Random().randint(0, 1)
          

class Group(BaseGroup):
    counter_female = models.IntegerField(initial = 0)
    counter_male = models.IntegerField(initial = 0)


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
    #variables on the HelperFunctions.py
    screenout = models.BooleanField(initial=0)
    quota = models.BooleanField(initial=0)

    #Welcome
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)
    time_start = models.StringField(initial='-999')
    eligible_question = models.IntegerField()

    #QuestianPage
    name_question = models.StringField(
        label= "<b>What is your name?</b>")
    age_question = models.IntegerField(
        label= "<b>What is your age?</b>", # allow just adults 
        min=18, 
        max=100
    )
    gender = models.IntegerField(initial=-999, blank=False)

    academic_level =models.IntegerField(initial=-999, blank=False)
    
    study_question = models.StringField(
        label= "<b>What is your study programm?</b> <br>(Please enter the full name in English.)")

    hidden_input = models.IntegerField(initial=50, blank=True)
    time_question = models.StringField(initial='-999')

    #Question picture 1
    lecture_question = models.StringField(
        label= "<b>What do you think is missing for lecture halls that are suitable for effective teaching?</b>")

    #Question picture 2
    seminar_question = models.StringField(
        label= "<b>What do you think is missing in seminar rooms for effective teaching?</b>")

    #PopoutPage
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')
                        
    #EndPage
    group_assignment = models.IntegerField() #the variable we declared on top
    
