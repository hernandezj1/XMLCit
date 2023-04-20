# This function extracts all citatio tags and then checks them for the preesence of ibid and op cit.
# Upon identification ti will check all preceding citatio to see if one has a fullcitation AND the id is the same
# If both conditions are TRUE it will add the citation

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
