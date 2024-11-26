from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 

class Welcome(Page):
    form_model = Player

#with the function before_next_page you can can control what should happen. It is a nice feature for filtering
#or also setting variables
    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1
    

class QuestionPage(Page):
    form_model = Player
    form_fields = ['age_question', 'name_question', 'gender', 'study_question', 'academic_level']
    

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
                QuestionPage,
                PopoutPage,
                PicturePage1,
                PicturePage2,           
                EndPage]