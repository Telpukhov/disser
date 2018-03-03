# coding: utf8

from lxml import etree
import zipfile

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





FA, FAA = get_comments(docxFileName)

import json
with open('array.txt', 'w') as outfile:
    json.dump(FAA, outfile)

for comment in FA:
    print(comment)
# здесь надо скопипастить из консоля в comments.txt