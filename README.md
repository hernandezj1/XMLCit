# XMLCit package

## Purpose
 
  This packages was developed by staff of the Research Computing Center to serve the needs of our digital humanities community. Therefore the classes and functions in this package were develop with ease of use and to be applicable to TEI-XML standards. TEI-XML specifications can be found here <a href='https://tei-c.org/'>TEI</a>
## Structure
  Due to the brevity of this package only a single module was made to hold one class( with 3 methoods) and 3 additional functions.
## Class description : Insert

  This class focuses on the insertion of attributes into tags in the XML.

### Method descriptions

1.  __ID__
      inserts an 'ID' attribute inside the selected tag based on text inside XML tag

2.  __CitbyID__
  - inserts a text( in this case meant to be a full citation) in an attrribute by the ID attribute

3.  __CitbyText__
- inserts a text( in this case meant to be a full citation) in an attrribute by seacrhing for matching text

## Additional Functions descriptions

4.  __AddVIAF__
        This function identifies those nodes (citations) in which a repeated non-written out citation happens like Ibid. and op. cit. 
        It will then transfer the closest fullcitation attribute from a node that has: the same ID number AND a FullCitation attribute. 

5.  __Addtag__
        This function adds an attribute with the VIAF ( Virtual International Authority File) number  of the citation. To do this it searches the first 4 words of the citation in the VIAF database using the selenium webdriver.
        
        
6. __RepeatCitation__
        This function adds a tag on a specified word inside an existing tag (node) in the XML. The Initial purpose of the function ( and the one contained in defaults) is to tag repeated citation with the cit tag for further inclusion of attributes with other functions in package
