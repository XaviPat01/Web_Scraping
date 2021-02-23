from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass


def captcha(qn:str)->int:
    words = list(qn.split())
    #print(words)
    numbers=[int(x) for x in words if x.isdigit()]
    if '+' in words:
        return (sum(numbers))
    elif '-' in words:
        return (numbers[0]-numbers[1])
    elif 'first' in words:
        return (numbers[0])
    elif 'second' in words:
        return (numbers[1])

# Establish chrome driver and go to report site URL
url = "https://moodle.iitd.ac.in/login/index.php"
driver = webdriver.Chrome()
driver.get(url)

user=input("Enter your user id: ")
pswd=getpass.getpass(prompt='Enter your password: ', stream=None)

search1 = driver.find_element_by_id("username")
search1.send_keys(user)
search2 = driver.find_element_by_id("password")
search2.send_keys(pswd)

cqn = driver.find_element_by_xpath("//form[text()[contains(.,'Please')]]")
#print(cqn.text)
cfield = driver.find_element_by_id("valuepkg3")
cfield.send_keys(captcha(cqn.text))

btn = driver.find_element_by_xpath('//input[@id="loginbtn"]')
btn.click()

time.sleep(10)
driver.quit()