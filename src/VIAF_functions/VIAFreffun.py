
def AddVIAF(filename:str, node:str, numberofwords:int, filepath:str,encoding:str='utf8',VIAFattribbute:str='VIAF', Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
        """
        Description
        ------------
        This function adds an attribute with the VIAF ( Virtual International Authority File) number  of the citation. To do this it searches the first 4 words of the citation in the VIAF database using the selenium webdriver.
        
        Output
        -------
        Outputs a file with the added attributes on the specified tags and their corresponding VIAF numbers. teh file will be encoded in UTF-8 with the stated namespace.
        
        Parameters
        ----------
        filename:str
            The file to be read in
        node:str
            XML node to be searched for the text. Also the node inside which the attrbute will be added. Searches in entire document.
        numberofwords:int
            Number of words to be selected from Citattribute text to be searched on VIAF search bar
        filepath:str
            filepath of the Chrome webdriver executable file on host system. Chrome must be installed to be able to use this function
        encoding:str
            encoding of the XML document 
            possible values:'unicode' ;'utf-8'
            defaultvalue='utf8'
        VIAFattribbute:str
            name of attribute to be added
            defaultvalue='VIAF'
        Citattribute:str
            name of attribute to be selected and searched on VIAF website
            defaultvalue='ID'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """  
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
        with open(filename, encoding) as f:
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

                    
                    elem.attrib[VIAFattribbute]=numbers

        outputfile= VIAFattribbute+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)

