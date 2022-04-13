# import required module
import os
from pip import main
import bs4
import hashlib
import random

import sys



#check if a directory exists
def isDir(directory):
    if not os.path.exists(directory) and not os.path.isabs(directory):
        print("Directory does not exist or is not absolute path")
        return False
    return True


#get number of times item is in list
def getCount(item, list):
    count = 0
    for i in list:
        if i == item:
            count += 1
    return count


# add id attribure to elemment if not existing
def addId(element, affectedElements,ids):
    if not element.has_attr('id'):
        print(element)
        hash = hashlib.sha1(
            (str(element)).encode("UTF-8")).hexdigest()
        similarid = getCount(hash, ids)
        ids.append(hash)
        
        if(similarid > 0 ): 
            hash = hashlib.sha1(
            (str(element) + str(similarid)).encode("UTF-8")).hexdigest()
        element['id'] = 'te-' + hash[:10]
        affectedElements += 1
        
    return affectedElements , ids


def getFileRawData(filePath):
    with open(filePath, "r", encoding="utf8") as f:
        return f.read()


def saveFile(filePath, data):
    with open(filePath, "w") as f:
        return f.write(data)


def main():
    ids = []
    affectedElements = 0
    # constants
    # tags that shold be edited
    TAGS = ['p', 'form', 'a', 'input', 'p', 'h1', 'h2',
            'h3', 'h4', 'h5', 'h6', 'label', 'span', 'select', 'div', 'button', 'li' , 'img', 'tr' , 'td', 'th', 'b' , 'i', 'u', 'strong', 'em', 'ol', 'ul', 'table', 'thead', 'tbody', 'tfoot', 'caption', 'colgroup', 'col', 'tr', 'td', 'th', 'img', 'video', 'audio', 'source', 'track', 'canvas', 'map', 'area', 'svg', 'math', 'iframe', 'object', 'embed', 'time', 'mark', 'wbr', 'textarea', 'noscript', 'style', 'script', 'head', 'title', 'meta', 'link', 'base', 'body', 'html']
    # assign directory
    DIRECTORY = sys.argv[1]

    # iterate over files in
    # that directory
    for root, dirs, files in os.walk(DIRECTORY):
        # iterate over files
        for filename in files:
            try:
                # filter files (chose only html files)
                if filename.endswith(".html"):
                    print("----------------------------------------------------")
                    print("                  " +
                          filename + "                  ")
                    print("----------------------------------------------------")
                    tempAffectedElements = affectedElements
                    print("opening file ...")
                    # get current file raw data
                    currentFileRawData = getFileRawData(
                        os.path.join(root, filename))
                    # parse file raw data
                    print("parsing ...")
                    soupedFile = bs4.BeautifulSoup(
                        currentFileRawData, 'html.parser')
                    # modify parsed file elements
                    for tag in TAGS:
                        elements = soupedFile.findAll(tag)
                        for element in elements:
                            affectedElements , ids = addId(element, affectedElements ,ids)
                    #print(os.path.join(root, filename))
                    print("saving...")
                    saveFile(os.path.join(root, filename),
                             soupedFile.prettify())
                    print("done")
                    print('afected elements: ' +
                          str(affectedElements - tempAffectedElements))
            except Exception as e:
                print(e)
    print(ids)
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    print('affected elements: ' + str(affectedElements))
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    

if __name__ == '__main__':
    
    if (len(sys.argv) > 1):
        
        if(isDir(sys.argv[1])):
            main()
    else:
        print('plese enter directory path')

