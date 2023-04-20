#This python file contains the following 3 functions: 
# function 1: insert ID based on the presence of a string of text
# function 2: Insert Citation based on ID number
# Function 3: Insert citation based on the presence of a string of text

class Insert:

    def __init__(self):
        pass
    

    def ID(self,filename:str, node:str , text:str , id:int, IDattribute:str='ID', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
    
        import xml.etree.ElementTree as ET
        
        #Opening file
        with open(filename, encoding='utf8') as f:
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



    def CitbyText(filename:str, node:str, citation:str, text:str, Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
    
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

