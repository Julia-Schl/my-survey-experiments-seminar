from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 


class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width', 'time_start']


class GenderPage(Page):    
    form_model = Player
    form_fields = ['gender']
                

class AgePage(Page):    
    form_model = Player
    form_fields = ['age_question']
                

class QuestionPage(Page):
    form_model = Player
    form_fields = ['name_question', 'study_question', 'academic_level', 'time_question']



class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player



class PopoutPage(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout']


class PicturePage1(Page):
    form_model = Player
    form_fields = ['lecture_question']
    def is_displayed(self):
        '''this is another otree specific function that regulates if a page is displayed or not '''
        #this will show the page to anybody who has the right assignment so in this case 
        return self.player.group_assignment == 1

class PicturePage2(Page):
    form_model = Player
    form_fields = ['seminar_question']
    def is_displayed(self):
        '''this is another otree specific function that regulates if a page is displayed or not '''
        #this will show the page to anybody who has the right assignment so in this case 
        return self.player.group_assignment == 0




#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                GenderPage,
                AgePage,
                QuestionPage,
                PopoutPage,
                PicturePage1,
                PicturePage2,           
                EndPage]
