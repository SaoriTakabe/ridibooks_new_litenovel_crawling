# ridibooks_new_litenovel_crawling

Prerequisite
- Python 3.X (Tested Python3.6)
- Selenium
- Chrome web driver( this file and list_update.py should be in the same directory)
- Slacker
- Slack bot token
- Tightvncserver

This script is crawling ridibooks's latest lite novel updates, save them to txt file in EC2 instance, and it to slack using crontab and slack bot 

1. Create Ubuntu EC2 instance

2. Setting Ubuntu EC2 GUI setting
(https://medium.com/@0xson/running-ubuntu-desktop-gui-aws-ec2-instance-on-windows-3d4d070da434)

3. Access EC2 using GUI

4. Install Selenium in Ubuntu ( sudo apt-get install python3-pip and then sudo pip install selenium)

5. Install Chrome in Ubuntu

        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
        sudo apt-get update
        sudo apt-get install google-chrome-stable
        sudo rm -rf /etc/apt/sources.list.d/google.list
        sudo apt-get clean
        sudo apt-get update
        
6. Downlaod chromedriver which version fits your current Chrome in Ubuntu (https://chromedriver.chromium.org/downloads)

7. Extract the downloaded chromedirver zip file in the same directory where list_update.py is located

8. Create a app inslack and update bot User OAuth Access Token info in list_update.py

9. Install Slacker (sudo pip install slacker)

10. Config crontab so that the bot can send updates daily

       . <hour> * * * export DISPLAY=:1 && cd <list_update.py file location> && /usr/bin/python3.6 list_update.py > list_update.log 2>&1
