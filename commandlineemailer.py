'''
Write a program that takes an email address and string of text
on the command line and then, using Selenium, logs into your
email account and sends an email of the string to the provided address.
(You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or Twitter account.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


email = input("What is your email address? ")
password = input("What's your password? ")
text = input("What is the message you want to send? ")

browser = webdriver.Chrome()
browser.get("https://www.gmail.com")

emailElem = browser.find_element_by_id("identifierId")
emailElem.send_keys(email)

emailnextButton = browser.find_element_by_xpath('//*[@id="identifierNext"]/content')
emailnextButton.click()

delay = 3 # seconds

pwdElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
pwdElem.send_keys(password);


pwdNextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
pwdNextButton.click()

composeElem = browser.find_element_by_xpath('')
hover = ActionChains(browser).move_to_element(composeElem)
hover.perform()

#actions = ActionChains(browser)
#actions.move_to_element(composeButton).click().perform()
#composeButton.click()

#composeElem =

#to = browser.find_element_by_xpath('//*[@id=":ob"]')
#to.send_keys(email)

