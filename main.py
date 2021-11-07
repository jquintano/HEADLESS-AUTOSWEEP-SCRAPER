from selenium import webdriver
import os
import time

# os.environ['PATH'] = r"C:\Selenium"

def getbalance():
    # driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    driver.get('https://autosweeprfidapps.com/balanceinquiry/')
    driver.implicitly_wait(20)
    time.sleep(2)
    acct_in = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/div[2]/div/form/div[1]/input')
    acct_in.send_keys('EMAIL') #autosweep user id
    time.sleep(2)
    acct_pass = driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/div[2]/div/form/div[2]/input')
    acct_pass.send_keys('PASSWD') #autosweep password
    time.sleep(2)
    driver.find_element_by_css_selector('button[class="btn btn-lg btn-info btn-block"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('button[class="btn btn-success btnBalance"]').click()
    time.sleep(10)
    pat = "//*[@id='modalBalance']/div/div/div[2]/h3"
    balance = driver.find_element_by_xpath(pat).get_attribute("innerHTML")
    if len(balance) > 0:
        return balance
    else:
        return 'Not Available'

def email_alert(subj, body, to):
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subj
    msg['to'] = to
    user = 'ALERT_MAIL'
    msg['from'] = user
    passwd = 'AM_PASSWD'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, passwd)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    myBalance = getbalance()
    email_alert(f"AUTOSWEEP BALANCE: {myBalance}", myBalance, 'EMAIL')
    # print(myBalance)
