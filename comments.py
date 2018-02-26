from lxml import etree
import zipfile
from pprint import  pprint

def tanimoto(s1, s2):
    a, b, c = len(s1), len(s2), 0.0
    for sym in s1:
        if sym in s2:
            c += 1
    return c / (a + b - c)

ooXMLns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
docxFileName = "main.docx"

def get_comments(docxFileName):
  docxZip = zipfile.ZipFile(docxFileName)
  commentsXML = docxZip.read('word/comments.xml')
  et = etree.XML(commentsXML)
  comments = et.xpath('//w:comment',namespaces=ooXMLns)
  FA = []
  FAA = {}
  ind = 0
  for c in comments:
    ind += 1
    comment = (c.xpath('string(.)'))
    arr = comment.split('$$$')
    tmp = [i for i in range(len(FA), len(FA)+len(arr))]
    FA += arr
    FAA[ind] = tmp
  return (FA, FAA)


  pprint(FA)
  pprint(FAA)

def clean_array(FA):
    for i in range(len(FA)):
        max = 0
        for j in range(i):
            cmp = tanimoto(FA[i], FA[j])
            if max < cmp:
                max = cmp
        print(str(i)+' - ', str(max))



FA, FAA = get_comments(docxFileName)
clean_array(FA)