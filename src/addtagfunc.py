
def Addtag(filename:str,text:str, node:str, tag:str, encoding:str='utf8', ns:dict={'default':'http://www.tei-c.org/ns/1.0'},):
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
        with open(filename, encoding) as f:
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

