from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

cnum= input("Enter the contest number: ")

options= Options()
options.headless = True
driver = webdriver.Chrome(options= options)

url=f"https://codeforces.com/contest/{cnum}"

os.mkdir(f'{cnum}')
driver.get(url)
l1=driver.find_elements_by_xpath("//td[contains(@class,\"id\")]//a")
l2=[x.text for x in l1]
for probcode in l2:
    urlprob=f'{url}/problem/{probcode}'
    driver.get(urlprob)
    folder=f'{cnum}/{probcode}'
    os.mkdir(folder)

    qn = driver.find_element_by_xpath('//div[@class="problem-statement"]')
    size = qn.size
    w, h = size['width'], size['height']
    driver.set_window_size(w+25,h+100)
    driver.execute_script("arguments[0].scrollIntoView();", qn)
    time.sleep(0.5)
    qn.screenshot(f'{folder}/problem.png')

    inputs=[inpt.text for inpt in driver.find_elements_by_xpath('//div[@class="input"]//pre')]
    for i in range(len(inputs)):
        with open(f'{folder}/input{i+1}.txt','w') as finput:
            finput.write(inputs[i])

    outputs=[otpt.text for otpt in driver.find_elements_by_xpath('//div[@class="output"]//pre')]
    for i in range(len(outputs)):
        with open(f'{folder}/output{i+1}.txt','w') as foutput:
            foutput.write(outputs[i])