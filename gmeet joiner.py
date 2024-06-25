from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui 
import time as t
import datetime

x = datetime.datetime.now()
y = datetime.datetime.now()
def gmail_login():
    dr.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin") 

    ele=dr.find_element_by_id('identifierId')
    ele.send_keys('') #your mail goes here
   
    btn=dr.find_element_by_id('identifierNext').click()
    
    password=dr.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.click()
    password.send_keys('') #your passwrod goes Here!

    nextButton = dr.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    WebElement element = dr.findElement(By.xpath('//*[@id ="passwordNext"]'));
    Actions actions = new Actions(dr);
    actions.moveToElement(element).click().build().perform();

def clss_login(url):
        print("Entering Google Meet: ")
        dr.get(url)
   
        t.sleep(12)
        webdriver.ActionChains(dr).key_down(Keys.CONTROL).send_keys("d").perform()
        print("Turned off Mike")
        t.sleep(2)
        webdriver.ActionChains(dr).key_down(Keys.CONTROL).send_keys("e").perform()
        print("Turned off Camera")

        print("Joining Class...")
        t.sleep(5)    
        xpath = '//span[text()="Join now"]/..'
        join_btn = WebDriverWait(dr, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        join_btn.click()
        print("Joined Class Successfully")
        print("---------------------------")
    
curr= datetime.datetime.now().time()


Classes={
              "Phy":""    #LInk for each class goes Here!
              ,"Chem":""
              ,"Maths":""
              ,"ME":""
              ,"CSE":""
              ,"English":""
              ,"eplabA":""
              ,"eplabB":""
              ,"Java":""
              ,"E&I":""
              ,"CG":""
              ,"plab":""
              ,"clab":""
        }
#time tale Goes Here!
Mon=[]
Tue=[]
Wed=[]
Thu=[]
Fri=[]
Sat=[]

#Time for each Hour goes here!
#if now >now.replace(hour=9, minute=30, second=00, microsecond=00) and now < now.replace(hour=10, minute=30, second=, microsecond=):
#if 1st hour is from 9:30 to 10:30
def first_hour(day):
    while True:
        now=datetime.datetime.now().time()
        if now >now.replace(hour=, minute=, second=00, microsecond=00) and now < now.replace(hour=, minute=, second=, microsecond=):
            url=Classes[day[0]]
            print("joining ",day[0]," class")
            clss_login(url)
            break
        t.sleep() #if u start  program early,the program waits till the specified time which consume battery and Memory,to avoid that pause the program for given time
                  #best reak time will be current time-required time.

def sec_hour(day):
    while True:
        
        now=datetime.datetime.now().time()
        if now >now.replace(hour=, minute=, second=00, microsecond=00) and now < now.replace(hour=, minute=, second=00, microsecond=00):
            url=Classes[day[1]]
            print("joining ",day[1]," class")
            clss_login(url)
            break
        t.sleep()
def third_hour(day):
    while True:
       
        now=datetime.datetime.now().time()
        if now >now.replace(hour=1, minute=, second=00, microsecond=00) and now < now.replace(hour=, minute=, second=00, microsecond=00):
            url=Classes[day[2]]
            print("joining ",day[2]," class")
            clss_login(url)
            break
        t.sleep()

def fourth_hour(day):
    while True:
      
        now=datetime.datetime.now().time()
        if now >now.replace(hour=13, minute=25, second=00, microsecond=00) and now < now.replace(hour=14, minute=20, second=00, microsecond=00):
            url=Classes[day[3]]
            print("joining ",day[3]," class")
            clss_login(url)
            break
        t.sleep()
def fifth_hour(day):
    while True:
      
        now=datetime.datetime.now().time()
        if now >now.replace(hour=, minute=, second=00, microsecond=00) and now < now.replace(hour=, minute=, second=00, microsecond=00):
            url=Classes[day[4]]
            print("joining ",day[4]," class")
            clss_login(url)
            break
        t.sleep()

def six_hour(day):
    while True:
      
        now=datetime.datetime.now().time()
        if now >now.replace(hour=, minute=, second=00, microsecond=00) :
            url=Classes[day[5]]
            print("joining ",day[5]," class")
            clss_login(url)
            break
        t.sleep(300) 

#this Function joins class based on Day
def join_class(day):
    p=periodCheck()
    print("This is Period No: ",p)
    if p==1:
       print("joining class At 9:40 AM") 
       first_hour(day)
       p+=1
    if p==2:
        print("joining class At 10:40 AM") 
        if(day!='Mon' or day!='Wed'):
            sec_hour(day)
        p+=1
    if p==3:
        print("joining class At 11:40 PM") 
        third_hour(day)
        p+=1
    if p==4:
        print("joining class At 13:30 PM") 
        fourth_hour(day)
        p+=1
    if p==5:
        print("joining class At 14:40 PM") 
        fifth_hour(day)
        p+=1
    if p==6:
        print("joining class At 15:40 PM") 
        six_hour(day)
        p+=1
    
#Comes Handy when you execute the program in between classes
def periodCheck():
    if curr.hour >=  or  (curr.hour ==  and curr.minute<40):
        p=1
    if (curr.hour ==  and curr.minute>=) or (curr.hour== and curr.minute<=): 
        p=2
    if (curr.hour ==  and curr.minute>=) or (curr.hour== and curr.minute<=):  
        p=3
    if ((curr.hour == ) or (curr.hour == ) and curr.minute>=) or (curr.hour== and curr.minute<=): 
        p=4
    if (curr.hour ==  and curr.minute>=) or (curr.hour==15 and curr.minute<=): 
        p=5
    if (curr.hour ==  and curr.minute>=) :
        p=6

    return p

#Getting day and time from Local System
day=(x.strftime("%a"))
time=x.strftime("%X")


print("This is an Automated Web Service fDevoloped and Maintained by 'AC# Devolopers'")
print("Confirming Day")
print("Is It Today",day)
res=input("[Y/N]: ")
print("Is There any Change In todays Schedule")
res1=input("[Y/N]: ")
if (res=='y' or res=='Y') and (res1=='n' or res1=="N"):

    print("Activating Automated Services....")
    opt=Options()
    opt.set_preference('dom.webnotifications.enabled', False)
    opt.set_preference ('media.navigator.permission.disabled', True)
    print("Initializing Web Drivers")
    dr=webdriver.Firefox(firefox_options=opt)
    print("Logging Into Google Account")
    gmail_login()
    print("Logged In Successfully")
    print("----------------------------")
    print("Joining Class as Scheduled")
    print(Classes)
    print("----------------------------")
    print("Todays Schedule Is")
    if day=="Mon":
        print(Mon)
        print("------------------------")
        join_class(Mon)
    if day=="Tue":
        print(Tue)
        print("------------------------")
        join_class(Tue)
    if day=="Wed":
        print(Wed)
        print("------------------------")
        join_class(Wed)
    if day=="Thu":
        print(Thu)
        print("------------------------") 
        join_class(Thu)
    if day=="Fri":
        print(Fri)
        print("------------------------") 
        join_class(Fri) 
    if day=="Sat":
        print(Sat)
        print("------------------------") 
        join_class(Sat)  
    print("-----------------------------")     
else:
    print("A Change in Schedule Or Error in system Date and Time...Please proceed manualy")  
