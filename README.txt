# ridibooks_new_litenovel_crawling

Prerequisite

        - Ubuntu (Ubuntu 20.0.4 LTS)
        - Python 3.X (Tested Python3.8.2)
        - Selenium
        - Chrome web driver( this file and list_update.py should be in the same directory)
        - Slacker
        - Slack bot token

This script is crawling ridibooks's latest lite novel updates, save them to txt file in GCP instance, and it to slack using crontab and slack bot 

1. Create Ubuntu GCP instance

2. Install pip3 in Ubuntu

        sudo apt-get install python3-pip

3. Install Selenium in Ubuntu 
        
        sudo pip3 install selenium)

4. Install Slacker 
        
        sudo pip3 install slacker

5. Install Chrome in Ubuntu

        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
        sudo apt-get update
        sudo apt-get install google-chrome-stable
        sudo rm -rf /etc/apt/sources.list.d/google.list
        sudo apt-get clean
        sudo apt-get update
        
6. Downlaod chromedriver which version fits your current Chrome in Ubuntu (https://chromedriver.chromium.org/downloads). The file name will be chromedriver_linux64.zip

7. Extract the downloaded chromedirver zip file in the same directory where list_update.py is located
        
        sudo apt-get install unzip
        unzip chromedriver_linux64.zip

8. Create a app inslack and update bot User OAuth Access Token info in list_update.py

9. Config crontab so that the bot can send updates daily. This config will run list_update.py (crawling latest litenovel lists from Ridibooks, sending them to your slack channel.) and then update list_update.log if there are standard errors.

       . [hour] * * * /usr/bin/python3.6 list_update.py [list_update.py file location] > list_update.log 2>&1
