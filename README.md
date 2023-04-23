# XMLCit package

## Purpose
 
  This packages was developed by staff of the Research Computing Center at Florida State University to serve the needs of our digital humanities community. Therefore the methods and functions in this package were developed with ease of use in mind and to be specifically applicable to TEI-XML standards. TEI-XML specifications can be found here <a href='https://tei-c.org/'>TEI</a>

  The functions and methods here encompassed modify XMl documents on a large scale to avoid tedious work by the researcher. The main goald of this package was to provide a way to do the following: 

  1. Tag a specific word within every instance of a specific node of the TEI-XMl document. In our case this was specific citations within the __note__ node.
  
  2. Add attributes to every instance of a specific node based on the presence of an ID number attribute or a specific collection of words inside said node. These attributes where:

      a. A VIAF number, webscraped from the VIAF website

      b. an ID number

      c. A completed citation. 
    

  __Usage guidelines:__

  To import the libary please use the next few lines in your code. It is key that for the methods inside the Insert class you define an instance of this class beforehand.

    ```
    from XMLCit import functions # After this all functions can be found by doing the following: 
    functions.AddVIAF
    functions.Addtag
    functions.RepeatCitation

    #To use the class methods do the following:
    instance = functions.Insert()
    #then you can use this instance to call each of the methods and not include the self parameter
    instance.ID()
    instance.CitbyID()
    instance.CitbyText()

    ```



## Structure
  Due to the brevity of this package only a single module was made to hold one class( with 3 methods) and the 3 additional functions.
## Class description : Insert

  This class focuses on the Insertion of attributes into tags in the XML documents.

### Method descriptions

1.  __ID__
  - Inserts an 'ID' attribute inside the selected tag based on text inside XML tag. 

2.  __CitbyID__
  - Inserts a text( in this case meant to be a full citation) in an attribute by checking for the specified ID number.

3.  __CitbyText__
  - Inserts a text( in this case meant to be a full citation) in an attrribute by seacrhing for matching text inside the selected tag (node)

## Additional Functions descriptions

4.  __AddVIAF__
      This function adds an attribute with the <a href='https://viaf.org/'>VIAF</a> (Virtual International Authority File) number of the cited text. To do this it searches the first 4 words of the citation in the VIAF database using the __selenium__ webdriver.

      *Additional Requirements:*
        This function will need a filepath argument to be filled in directing the fucntion to find a chromedriver executable file to run the __selenium__ webdriver. This version of the function only works with the Chrome web browser. Future updates shall expand to the Firefox webdriver.       

      
5.  __Addtag__

      This function adds a tag on a specified word inside an existing tag (node) in the XML. The Initial purpose of the function (and the one contained in defaults) is to tag a specific word with the __cit__ tag that is inside a specific tag  for further inclusion of attributes with other functions in this package.

6. __RepeatCitation__

      This function identifies those nodes (in this case __cit__ tags) in which a repeated non-written out citation happens like Ibid. and op. cit. It will then transfer the closest Full Citation attribute from a node that has: the same ID number AND a completed FullCitation attribute. It can also be used to transfer the VIAF attributes as well by changing the FullCitation default