from selenium import webdriver
from slacker import Slacker #send a messate slack
slack = Slacker('your bot token start with xoxb-')
import datetime #add time info

f = open('new_lists.txt','w')

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome('/home/ubuntu/ridibooks/chromedriver')

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
