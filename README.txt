What Is This?
-------------

The script logs on to autosweep account, get the
balance and send it through gmail via headless browser.
Deployed to heroku and added a scheduler.

How To Use
-----------------------
1. Log in to heroku and create a new app

2. On settings declare the following config vars:
    ALERT_MAIL (your gmail sender)
    AM_PASSWD (your gmail password)
    CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
    EMAIL (your AUTOSWEEP account log in username)
    PASSWD (your AUTOSWEEP account log in password)

3. Add buildpack:
    heroku/python
    https://github.com/heroku/heroku-buildpack-google-chrome
    https://github.com/heroku/heroku-buildpack-chromedriver

4. Deploy

5. On overview, select configure add-ons and add it then set your scheduler


