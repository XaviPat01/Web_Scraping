from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Establish chrome driver and go to report site URL
url = "https://moodle.iitd.ac.in/login/index.php"
driver = webdriver.Chrome()
driver.get(url)

user=input("Enter your user id")
pswd = input("Enter your password")