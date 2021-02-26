#bonus_2
from selenium import webdriver
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def pcode(a:str)->str:
    if a[-1].isdigit():
        return a[-2:]
    else:
        return a[-1:]

def pset(a:str)->str:
    if a[-1].isdigit():
        return a[:-2]
    else:
        return a[:-1]

def probonpg(pagenum:int):
    urlnew=f"https://codeforces.com/problemset/page/{pagenum}?order=BY_RATING_DESC&tags={mindiff}-{maxdiff}"
    driver.get(urlnew)
    problist=driver.find_elements_by_xpath("//td[contains(@class,\"id\")]/a")
    probname=[prob.text for prob in problist]
    for problem in probname:
        probcode=pcode(problem)
        probset=pset(problem)
        folder=f"{probset}_{probcode}"
        os.mkdir(folder)
        urlprob=f"https://codeforces.com/problemset/problem/{probset}/{probcode}"
        driver.get(urlprob)
        qn = driver.find_element_by_xpath('//div[@class="problem-statement"]')

        size = qn.size
        w, h = size['width'], size['height']
        driver.set_window_size(w+25,h+100)
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


maxdiff = int(input("Enter the maximum difficulty level:"))
mindiff = int(input("Enter the minimum difficulty level:"))

options=Options()
options.headless=True
driver = webdriver.Chrome(options=options)
url=f"https://codeforces.com/problemset?order=BY_RATING_DESC&tags={mindiff}-{maxdiff}"
driver.get(url)

#https://codeforces.com/problemset?order=BY_RATING_DESC&tags=

if mindiff>maxdiff:
    print("The difficulty values given are invalid.")

else:
    try:
        driver.find_element_by_xpath("//table[@class=\"problems\"]//tr[@class=\"no-items visible\"]//td")
        print("The given range contains no problems. Kindly also check if it's valid or not.")
        print("exiting")
        cond = False
        driver.quit()
    except NoSuchElementException:
        cond= True      

    if cond:
        try:
            pages=driver.find_elements_by_xpath("//span[@class=\"page-index\"]/a")
            pgend=int(pages[-1].text)
            pgnum=1
            while pgnum<=pgend:
                probonpg(pgnum)
                pgnum+=1
        except:
            probonpg(1)


#//span[@class="ProblemRating"]/parent::td/parent::tr/td   

