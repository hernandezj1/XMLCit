# This function extracts all citatio tags and then checks them for the preesence of ibid and op cit.
# Upon identification ti will check all preceding citatio to see if one has a fullcitation AND the id is the same
# If both conditions are TRUE it will add the citation

def RepeatCitation(filename:str, node:str, numbercits:int=5, tagwords:list={"op.",'Op.','Ibid.','Ibid','ibid.','ibid'}, Citattribute:str='FullCitation', IDattribute:str='ID'):
    

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
