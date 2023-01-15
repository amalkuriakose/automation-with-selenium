from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='./chromedriver')
 
chrome_browser = webdriver.Chrome(service=service)
 
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('Hello')

time.sleep(2)
button.click()
time.sleep(2)

output_message = chrome_browser.find_element(By.ID, 'display')

assert 'Hello' in output_message.text

time.sleep(2)