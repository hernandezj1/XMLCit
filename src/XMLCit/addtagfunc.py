#This python notebook adds a tag to any part of text, done here for the note node and adding <cit> tags to all Journal entries

def Addtag(filename:str,text:str, node:str, tag:str, ns:dict={'default':'http://www.tei-c.org/ns/1.0'},):
    import xml.etree.ElementTree as ET

    #Opening file
    with open(filename, encoding='utf8') as f:
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

