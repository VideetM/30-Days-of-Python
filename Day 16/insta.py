"""import getpass

my_password = getpass.getpass("What is your Password?\n")

print(my_password)"""

from selenium import webdriver
from conf import insta_user,insta_pass
import time

browser = webdriver.Chrome()

url = 'https://www.instagram.com'
browser.get(url)

time.sleep(2) 

user_el = browser.find_element_by_name("username")
user_el.send_keys(insta_user)
time.sleep(1)

pass_el = browser.find_element_by_name("password")
pass_el.send_keys(insta_pass)

time.sleep(1)

login_el = browser.find_element_by_css_selector("button[type='submit']")

login_el.click()
time.sleep(1)

