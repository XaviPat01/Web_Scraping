from selenium import web.driver
import time
from selenium.webdriver.common.by import By

data = input("Enter the file name and the contest number: ")
cnum = data.split()[-1]

url = "https://codeforces.com/problemset"
driver = webdriver.Chrome()
#https://codeforces.com/problemset 
# find_elements xpath= //a[text()[contains(.,cnum)]]
# OR driver.findElement(By.linkText(cnum))
# #
#iterate in the list. list
#on each element page xpath = //div[@class="problem-statement"]
#element.screenshot('path_of_file/filename.png')

#if not on current page: pages = find_elements_by_xpath: //a[@href[contains(.,'problemset/page')]] 
# click on pages[2]
# #