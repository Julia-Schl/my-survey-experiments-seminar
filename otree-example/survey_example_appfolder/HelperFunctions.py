import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number



'''
we also want to implement some functions to help with the quota checking and 
to have an overwview (counting) who is taking part in our survey.

Generally when it comes to redirecting we distinguish between people who: 
1. took part in the whole survey (and get redirected as success to the provider)
2. people who get screened-out (meaning they did not fulfill a characteristic one agreed upon previously)
3. people who get redirected because the quota is already full

We encode those three different event in three different variables (booleans) to use for redirecting

'''

def detect_screenout(self):
    '''this function will check for characteristics a participant needs to 
    take part in the survey, (f.e. a certain age or being eligible to vote)'''

    #if self.player.eligible_question == 2: # screen out anybody that is not eligible
        #self.player.screenout = 1
    
    if self.player.age_question >= 40:
        self.player.screenout = 1



def detect_quota(self):
    '''this function will check if a quota is already filled'''
    participant_number_male = self.group.counter_male
    participant_number_female = self.group.counter_female

    self.player.quota_male = 0
    self.player.quota_female = 0
    
    #declare quota reached if we have more than 1 participant that started
    if participant_number_male > 8:
        self.player.quota_male = 1

    if participant_number_female > 8:
        self.player.quota_female = 1
    return None


# def participant_count(self):
#     '''if we want to count different things we might also implement a function here.
#     For now we are just using the counter we implemented before'''
#     return None