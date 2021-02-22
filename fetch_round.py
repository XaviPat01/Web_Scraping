from selenium import webdriver
import os
import ctypes
import time
#from selenium.webdriver.common.by import By


def pname(a:str)->str:
    if a[-1].isdigit():
        return a[-2:]
    else:
        return a[-1:]
def pset(a:str)->str:
    if a[-1].isdigit():
        return a[:-2]
    else:
        return a[:-1]


cnum = input("Enter the contest number: ")

url = "https://codeforces.com/problemset"
driver = webdriver.Chrome()
driver.get(url)
exitcond = False
os.mkdir(f'{cnum}')
pgnum=1
while not exitcond:
    if driver.find_elements_by_xpath(f'//td[contains(@class,"id")]/a[text()[contains(.,{cnum})]]') and pset(driver.find_elements_by_xpath(f'//td[contains(@class,"id")]/a[text()[contains(.,{cnum})]]')[0].text)==cnum:
        j=0
        while j<2:
            driver.get(f'https://codeforces.com/problemset/page/{str(pgnum+j)}')
            problemset=driver.find_elements_by_xpath(f'//td[contains(@class,"id")]/a[text()[contains(.,{cnum})]]')
            exitcond= True
            namelist=[problem.text for problem in problemset]
            #print(namelist)
            plong=len(namelist)
            for i in range(0,plong):
                qname=pname(namelist[i])
                folder=f'{cnum}/{qname}'
                os.mkdir(folder)
                urlnew = f'https://codeforces.com/problemset/problem/{cnum}/{qname}'
                driver.get(urlnew)
                driver.maximize_window()
                qn = driver.find_element_by_xpath('//div[@class="problem-statement"]')
                driver.execute_script("arguments[0].scrollIntoView();", qn)
                driver.execute_script("document.body.style.zoom=40%")
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

            j+=1

    elif int(pset(driver.find_element_by_xpath('//td[contains(@class,"id")]//a').text))<int(cnum):
        exitcond=True
        os.rmdir(f'{cnum}')
        driver.quit()
        print("The requested contest doesn't exist!")
        #Error Box -----> ctypes.windll.user32.MessageBoxW(0, "The requested contest doesn't exist!", "Incorrect Contest Number",16)
    
    else:
        pgnum+=1
        urlnext = f'https://codeforces.com/problemset/page/{str(pgnum)}'
        driver.get(urlnext)

#https://codeforces.com/problemset 
# find_elements xpath= //a[text()[contains(.,cnum)]]
# OR driver.findElement(By.linkText(cnum))

#iterate in the list. list
#on each element page xpath = //div[@class="problem-statement"]
#element.screenshot('path_of_file/filename.png')

#if not on current page: pages = find_elements_by_xpath: //a[@href[contains(.,'problemset/page')]] 
# click on pages[1]