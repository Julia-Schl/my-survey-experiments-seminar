from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import string

import time

### change this link to the current session link
# this is the session wide link 
link = 'http://localhost:8000/join/jukolohe'

def build_driver():
    # Set up the driver
    return webdriver.Chrome() #(ChromeDriverManager().install())
    

# session is full
def detect_session_full(driver):
    try:
        driver.find_element(By.XPATH,  '//*[@id ="form"]/div/button')
        return False
    except NoSuchElementException:
        return True
    
# detect screenout age 
def detect_screenout_age(driver):

    elements = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='gender']")
    
    if elements:
        print('no screen-out')
        return False  
    else:
        print('screenout')
        return True 

# detect screenout gender
def detect_screenout_gender(driver):
    elements_gender = driver.find_elements(By.XPATH, '//*[@id="id_name_question"]')
    if elements_gender:
        print('no screen-out')
        return False  
    else:
        print('screenout')
        return True


def welcome_page(driver):
    # next button
    print('welcome page done')
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()


def age_page(driver):
    xpath_age = "//*[@id='id_age_question']"
    age = random.randint(18,42) # person cannot be under 18 
    driver.find_element(By.XPATH, xpath_age).send_keys(str(age))
    # next
    print('age page done')
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()
    


def gender_page(driver):
    gender = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='gender']")
    rand_selection = random.randint(0, len(gender) - 1)
    gender[rand_selection].click()
    # next
    print('gender page done')
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()
    


def question_page(driver):
    # name 
    xpath_name = '//*[@id="id_name_question"]'
    input_name = random.choice(['Lena', 'Max', 'Julia', 'Lukas', 'Benjamin', 'Kate'])
    driver.find_element(By.XPATH, xpath_name).send_keys(str(input_name))

    # degree 
    degree = driver.find_elements(By.NAME, 'academic_level')
    rand_selection = random.randint(0, len(degree) - 1)
    degree[rand_selection].click()

    # study program
    xpath_program = '//*[@id="id_study_question"]'
    input_program = random.choice(['SEDS', 'PolVer', 'Bio', 'Chemie', 'WiWi', 'LKM', 'Psycho'])
    driver.find_element(By.XPATH, xpath_program).send_keys(str(input_program))

    # next
    print('question page done')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()

#handle popout questions
def popout_page(driver):
    yes = '//*[@id="courseYes"]'
    no = '//*[@id="courseNo"]'
    select = random.randint(0, 1)

    input_text = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    
    if select == 0:
        driver.find_element(By.XPATH, yes).click()
        driver.find_element(By.XPATH, '//*[@id="divYes"]/input').send_keys(input_text)

    else:
        driver.find_element(By.XPATH, no).click()
        driver.find_element(By.XPATH, '//*[@id="divNo"]/input').send_keys(input_text)

    # next
    print('popout page done')
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()
    


def scroller(driver, element):
    driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
    time.sleep(0.3)  # short pause to stabilize 
    element.click()

def picture_pages(driver):
    
    try: 
        xpath_seminar = '//*[@id="id_seminar_question"]'
        seminar_element = driver.find_element(By.XPATH, xpath_seminar)
        scroller(driver, seminar_element)
        input_seminar = random.choice(['sockets', 'working technique', 'space for bags'])
        seminar_element.send_keys(str(input_seminar))
        print('seminar page detected and done')

    except:
        print('no seminar picture page')

    try:
        xpath_lecture = '//*[@id="id_lecture_question"]'
        lecture_element = driver.find_element(By.XPATH, xpath_lecture)
        scroller(driver, lecture_element)
        input_lecture = random.choice(['sockets', 'working technique', 'space for bags'])
        lecture_element.send_keys(str(input_lecture))
        print('lecture page detected and done')

    except: 
        print('no lecture picture page')
    
    #next 
    print('picture page done')
    next_button = driver.find_element(By.XPATH, '//*[@id="form"]/div/button')
    next_button.click()
    


def end_page(driver):
    # submit answers button
    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()
    print('end page done')

def run_bots(n_times, link):
    driver = build_driver()  # initialize the driver
    for i in range(n_times):  # go through the survey several times
        driver.get(link)  # open the browser to the url of your survey

        try:
            # full session 
            if detect_session_full(driver):
                print(f'For bot {i+1} the session is full.')
                break  

            welcome_page(driver)
            age_page(driver)
            
            # screenout due to age 
            if detect_screenout_age(driver):
                print(f'Bot {i+1} got a screenout page due to an age over 40.')
                continue
            
            gender_page(driver)

            # screenout due to gender
            if detect_screenout_gender(driver):
                print(f'Bot {i+1} got a screenout page due to a full gender quota.')
                continue

            question_page(driver)
            popout_page(driver)
            picture_pages(driver)
            end_page(driver)
            print(f'Bot_{i+1} passed successfully.')

        except Exception as e:
            print(f"Bot_{i+1} encountered an error: {e}")

# test with one bot too much
run_bots(n_times=21, link=link)
