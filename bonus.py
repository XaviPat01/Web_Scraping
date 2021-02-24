#Bonus problems
from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options

def pnum(s1:str)->int:
    idx=s1.rfind('/')
    return(s1[idx+1:])

num= int(input("Enter the number of past contests: "))

options=Options()
options.headless=True
driver = webdriver.Chrome(options=options)
url="https://codeforces.com/contests"
driver.get(url)


# //td[contains(@class,\"left\")]//a[text()[contains(.,\"Enter\")]]

l1=driver.find_elements_by_xpath("//td[contains(@class,\"left\")]//a[text()[contains(.,\"Enter\")]]")
l2=[l1[i].get_attribute("href") for i in range(0,num)]
#print(l2)
for urlcnum in l2:
    cnum=pnum(urlcnum)
    os.mkdir(f'{cnum}')
    driver.get(urlcnum)
    l3=driver.find_elements_by_xpath("//td[contains(@class,\"id\")]//a")
    l4=[x.text for x in l3]
    for probcode in l4:
        time.sleep(0.5)
        urlprob=f'{urlcnum}/problem/{probcode}'
        driver.get(urlprob)
        folder=f'{cnum}/{probcode}'
        os.mkdir(folder)

        qn = driver.find_element_by_xpath('//div[@class="problem-statement"]')
        size = qn.size
        w, h = size['width'], size['height']
        driver.set_window_size(w,h)
        driver.execute_script("arguments[0].scrollIntoView();", qn)
        #time.sleep(0.5)
        qn.screenshot(f'{folder}/problem.png')

        inputs=[inpt.text for inpt in driver.find_elements_by_xpath('//div[@class="input"]//pre')]
        for i in range(len(inputs)):
            with open(f'{folder}/input{i+1}.txt','w') as finput:
                finput.write(inputs[i])

        outputs=[otpt.text for otpt in driver.find_elements_by_xpath('//div[@class="output"]//pre')]
        for i in range(len(outputs)):
            with open(f'{folder}/output{i+1}.txt','w') as foutput:
                foutput.write(outputs[i])

