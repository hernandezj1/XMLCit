class Insert:
    """
    This class is part fo the XMLCit package which was designed to help reearhers using the TEI-XML standard to modify their XML, particularly their citations
    The Insert class inserts specific attributes XML tags based on particular existing attributes or the text contained within said tag. 
    The default namespace of the XMl is TEI and should be changed for other namespaces.

    Methods
    --------

    ID 
        - inserts an 'ID' attribute inside the selected tag based on text inside XML tag
    CitbyID
        - inserts a text( in this case meant to be a full citation) in an attrribute by the ID attribute
    CitbyText
        - inserts a text( in this case meant to be a full citation) in an attrribute by seacrhing for matching text
    """
    def __init__(self):
        pass
    

    def ID(self,filename:str, node:str , text:str , id:int, IDattribute:str='ID', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
        """
        Parameters
        ----------
        filename:str
            The file to be read in
        node:str
            XML node to be searched for the text. Also the node inside which the attrbute will be added. Searches in entire document.
        text:str
            Text to be checked for to match
        id:int
            id number assigned to the new attribute
        encoding:str
            encoding of the XML document 
            possible values:'unicode' ;'utf-8'
            defaultvalue='utf8'
        IDattribute:str
            name of inserted attribute
            defaultvalue='ID'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """
        import xml.etree.ElementTree as ET
        
        #Opening file
        with open(filename, encoding='UTF-8') as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if text in elem.text: 
                elem.attrib[IDattribute]= str(id)

        outputfile= 'new'+filename

        tree.write(outputfile, encoding='UTF-8', xml_declaration=True)



    def CitbyID(self,filename:str, node:str, citation:str, id:int, IDattribute:str='ID', Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
        """
        Parameters
        ----------
        filename:str
            The file to be read in
        node:str
            XML node to be searched for the text. Also the node inside which the attrbute will be added. Searches in entire document.
        citation:str
            Text (citation) to be inserted in new attribute
        id:int
            id number to be looked for
        encoding:str
            encoding of the XML document 
            possible values:'unicode' ;'utf-8'
            defaultvalue='utf8'
        IDattribute:str
            name of attribute to be matched
            defaultvalue='ID'
        Citattribute:str
            name of new attribute to be added
            defaultvalue='FullCitation'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """
        import xml.etree.ElementTree as ET
        
        #Opening file
        with open(filename, encoding='utf8') as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if IDattribute in elem.attrib and elem.attrib[IDattribute] == str(id): 
                elem.attrib[Citattribute] = citation

        outputfile= 'new'+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)



    def CitbyText(self,filename:str, node:str, citation:str, text:str, Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
        """
        Parameters
        ----------
        filename:str
            The file to be read in
        node:str
            XML node to be searched for the text. Also the node inside which the attrbute will be added. Searches in entire document.
        citation:str
            Text (citation) to be inserted in new attribute
        text:str
            Text to be checked for to match
        encoding:str
            encoding of the XML document 
            possible values:'unicode' ;'utf-8'
            defaultvalue='utf8'
        Citattribute:str
            name of new attribute to be added
            defaultvalue='FullCitation'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """
        import xml.etree.ElementTree as ET
        
        #Opening file
        with open(filename, encoding='utf8') as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if text in elem.text: 
                elem.attrib[Citattribute] = citation

        outputfile= 'new'+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)


def RepeatCitation(filename:str, node:str, numbercits:int=5, tagwords:list={"op.",'Op.','Ibid.','Ibid','ibid.','ibid'}, Citattribute:str='FullCitation', IDattribute:str='ID'):
        """
         Description
        ------------
        This function identifies those nodes (citations) in which a repeated non-written out citation happens like Ibid. and op. cit. 
        It will then transfer the closest fullcitation attribute from a node that has: the same ID number AND a FullCitation attribute. 

        Usage Tips
        ----------    
            Can be changed to add the VIAF attribute instead of the FullCitation attribute byy changing the Citattribute.
        Output
        -------
        Outputs a file with the added attributes on the specified tags and their corresponding citations on those repeated citations. The file will be encoded in UTF-8 with the stated namespace.
        
        Parameters
        ----------
        filename:str
            The file to be read in
        node:str
            XML node to be searched for the text. Also the node inside which the attribute will be added. Searches in entire document.
        numbercits:int
            Number of citations it will check before the node it is adding the citation to
        tagwords:list
            List of string that will be chked to identity the node as one to be modified by function. teh default identifie the concventions of Ibid. and Op. Cit
            These conventions are used because they are the most commonn way to cit in text a previously cited text.
            defaultvalue= ={"op.",'Op.','Ibid.','Ibid','ibid.','ibid'}
        IDattribute:str
            name of attribute to be matched
            defaultvalue='ID'
        Citattribute:str
            name of new attribute to be added
            defaultvalue='FullCitation'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """

        import sys
        import xml.etree.ElementTree as ET
        from xml.dom.minidom import parse
        from xml.dom.minidom import Node
        import codecs

        tree = parse(filename)
        a=tree.getElementsByTagName(node) # extracts all citations
        for elem in a:
            element=elem.firstChild.nodeValue # element that is being checked for presence of Ibid or Op cit
            string=str(element)
            for i in tagwords: 
                if i in string:
                    indexofelement=a.index(elem)
                    for h in range(0,numbercits):
                        try: 
                            index=(indexofelement-h) # Determines which of the previous cit tags it is editing
                            if a[index].hasAttribute(Citattribute) and a[index].getAttribute(IDattribute)==a[indexofelement].getAttribute(IDattribute):
                                citation=a[index].getAttribute(Citattribute)
                                a[indexofelement].setAttribute(Citattribute,citation)
                        except:
                            pass

        outputfile= 'new'+filename

        f = codecs.open(outputfile, mode='w', encoding='utf-8')
        f.write(tree.toxml("UTF-8").decode('utf-8'))
        f.close()


def AddVIAF(filename:str, node:str, numberofwords:int, filepath:str,VIAFattribbute:str='VIAF', Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
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

                    
                    elem.attrib[VIAFattribbute]=numbers

        outputfile= VIAFattribbute+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)


def Addtag(filename:str,text:str, node:str, tag:str, ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
        """
        Description
        ------------
        This function adds a tag on a specified word inside an existing tag (node) in the XML
        Initial purpose is to tag repeated citatiosn with the cit tag for further inclusion fo attributes with other functions in package

        Output
        -------
        Outputs a file with the added tags inside the specified node
        
        Parameters
        ----------
        filename:str
            The file to be read in
        text:str
            Text to be checked for to match
        node:str
            XML node to be searched for the text. Also the node inside which the attrbute will be added. Searches in entire document.
        tag:str
            name of tag to be inserted around text
        encoding:str
            encoding of the XML document 
            possible values:'unicode' ;'utf-8'
            defaultvalue='utf8'
        ns:dict
            namespace of the XML document
            defaultvalue= {'default':'http://www.tei-c.org/ns/1.0'}

        """  
   
        import xml.etree.ElementTree as ET

        #Opening file
        with open(filename, encoding='UTF-8') as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #this adds the cit to the Journal entry
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
                try:
                    if text in elem.text: 
                            complete=elem.text.replace('\n','')
                            string='<'+tag+'>'+text+'</'+tag+'>'
                            complete1=complete.replace(text,string)
                            complete2=''.join(['<note>',complete1,'</note>'])
                            tree2=ET.fromstring(str(complete2))
                            elem.text=''
                            elem.append(tree2)
                except: 
                    pass
        
        outputfile= 'new'+filename

        tree.write(outputfile, encoding='UTF-8',xml_declaration=True)

