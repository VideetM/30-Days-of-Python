from selenium import webdriver
import time


browser = webdriver.Chrome()

url = 'https://google.com'
browser.get(url)

"""<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" " data-ved="0ahUKEwjXzKn_koLrAhX2knIEHd7VAU0Q39UDCAY">
"""

time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name("q")
search_el.send_keys("selenium python")

"""
<input class="gNO89b" name="btnK" type="submit" data-ved="0ahUKEwjrlcnAlYLrAhWahXIEHWx_CakQ4dUDCA0">

"""
submit_button = browser.find_element_by_css_selector("input[type='submit']")
print(submit_button.get_attribute('name'))
time.sleep(2)
submit_button.click()
