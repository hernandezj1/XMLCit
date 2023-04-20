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
    

    def ID(self,filename:str, node:str , text:str , id:int, encoding:str='utf8', IDattribute:str='ID', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
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
        with open(filename, encoding) as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if text in elem.text: 
                elem.attrib[IDattribute]= str(id)

        outputfile= 'new'+filename

        tree.write(outputfile, encoding='UTF-8', xml_declaration=True)



    def CitbyID(self,filename:str, node:str, citation:str, id:int, encoding:str='utf8', IDattribute:str='ID', Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
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
        with open(filename, encoding) as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if IDattribute in elem.attrib and elem.attrib[IDattribute] == str(id): 
                elem.attrib[Citattribute] = citation

        outputfile= 'new'+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)



    def CitbyText(filename:str, node:str, citation:str, text:str, encoding:str='utf8', Citattribute:str='FullCitation', ns:dict={'default':'http://www.tei-c.org/ns/1.0'}):
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
        with open(filename, encoding) as f:
            tree = ET.parse(f)
            root = tree.getroot()

        #This section finds the element to be changed by selecting the node
        selector='.//{*}'+ node
        for elem in root.findall(selector, ns):
            if text in elem.text: 
                elem.attrib[Citattribute] = citation

        outputfile= 'new'+filename
        tree.write(outputfile,encoding='UTF-8', xml_declaration=True)

