from selenium import webdriver
from slacker import Slacker #send a messate slack
slack = Slacker('your bot token start with xoxb-')
import datetime #add time info
f = open('new_lists.txt','w')
myoptions = webdriver.ChromeOptions()
myoptions.add_argument('--incognito')
myoptions.add_argument('--disable-gpu')
myoptions.add_argument("--start-maximized")
myoptions.add_argument("--no-sandbox")
myoptions.add_argument('window-size=1920x1080') #for headless mode
myoptions.add_argument('headless') #for headless mode
driver = webdriver.Chrome('/home/lsh41610/ridibooks_new_litenovel_crawling/chromedriver', options=myoptions) #add parmeter options=[webdriver chrome options]
dt = datetime.datetime.now() #add time info
try:
    driver.get('https://ridibooks.com/category/new-releases/3000?order=recent') #crawling lite novel new-release page using h3 tag
    lists = driver.find_elements_by_tag_name('h3')
    f.write(dt.strftime("%A %d. %B %Y")) #add time info
    for novel in lists:
        head = novel.text
        print(head)
        f.write(head+'\n')
    f.close()
    r = open('new_lists.txt','r')
    title = r.read()
    slack.chat.post_message('#ridibooks', title)
    r.close()
except Exception as e:
    print(e)
    f.close()
finally:
    driver.quit()
~                              
