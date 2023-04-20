#this python file adds the corresponding VIAF numbers to each citation


def AddVIAF(filename:str, node:str, numberofwords:int, filepath:str, Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):

    # installations of webdriver
    from pickle import TRUE
    from tkinter.tix import Select
    from types import NoneType
    from attr import NOTHING
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait 
    import time
    import pandas as pd
    import os
    import sys
    import csv
    from bs4 import BeautifulSoup
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver import FirefoxOptions
    import xml.etree.ElementTree as ET




    #Opening file
    with open(filename, encoding='utf8') as f:
        tree = ET.parse(f)
        root = tree.getroot()

    #find the key terms to search VIAF database
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if Citattribute in elem.attrib: 
                string=elem.attrib[Citattribute]
                z=' '.join(string.split()[:numberofwords])
                
# Identify key terms to be looked for

                #initalize chromedriver
                driver = webdriver.Chrome(filepath)
                # Selection of website
                driver.get('https://viaf.org/')

                searchbar=driver.find_element(By.ID,'searchTerms')

                #Write on text bar
                searchbar.send_keys(z)

                # Find search button
                searchbutton=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div/form/fieldset[4]/input')
                driver.implicitly_wait(25)

                # click on button
                driver.execute_script("arguments[0].click();", searchbutton)
                driver.implicitly_wait(25)

                entry=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/a')

                driver.execute_script("arguments[0].click();", entry)
                driver.implicitly_wait(25)

                result=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[1]/div/h1[1]')
                a=result.get_attribute("innerHTML")

                numbers = "".join([ele for ele in a if ele.isdigit()])

                
                elem.attrib['VIAF']=numbers

    outputfile= 'VIAF'+filename
    tree.write(outputfile,encoding='UTF-8', xml_declaration=True)

