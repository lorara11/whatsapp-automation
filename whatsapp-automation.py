import time
import json
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_browser = Chrome(executable_path= os.getcwd() + '/chromedriver_linux64/chromedriver', options=chrome_options)
chrome_browser.get("https://web.whatsapp.com/")

time.sleep(30)

with open('./files/b12.json', 'r') as data_file:
    data = json.load(data_file)
    name = data['name']
    message = data['message']

chrome_browser.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

time.sleep(10)
chrome_browser.close()
