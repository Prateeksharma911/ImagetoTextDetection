from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("http://127.0.0.1:5000/")
#to identify element
s = driver.find_element_by_xpath("//input[@type='file']")
#file path specified with send_keys
s.send_keys("/Users/harsh/Downloads/Flask/captone-env/images/alt.jpg")
s2 = driver.find_element_by_name("button3")
s2.submit()
