from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

def pname(a:str)->str:
    if a[-1].isdigit():
        return a[-2:]
    else:
        return a[-1:]

cnum = "1486"

url = "https://codeforces.com/problemset"

chrome_options = webdriver.ChromeOptions() 
driver = webdriver.Chrome()
driver.get(url)


if driver.find_elements_by_xpath(f"//a[text()[contains(.,{cnum})]]"):
        found= True
        problemset = driver.find_elements_by_xpath(f"//a[text()[contains(.,{cnum})]]")
        for problem in problemset:
            problemnum=problem.text
            qname=pname(problemnum)
            os.mkdir(qname)
            problem.click()
            driver.maximize_window()
            time.sleep(2)
            qn = driver.find_element_by_xpath('//div[@class="problem-statement"]')
            qn.screenshot(f'{qname}/problem.png')

            sampinput=driver.find_element_by_xpath('//div[@class="input"]').find_element_by_tag_name('pre').get_attribute("innerHTML")
            with open(f'{qname}/input.txt','w') as finput:
                finput.write(sampinput)

            sampoutput=driver.find_element_by_xpath('//div[@class="output"]').find_element_by_tag_name('pre').text
            with open(f'{qname}/output.txt','w') as foutput:
                foutput.write(sampoutput)
            driver.get(url)