'''
Created on May 13, 2013

@author: Lucas
'''
import urllib
import re
import os

if __name__ == '__main__':
    baseURL = 'http://www.beautifulfractals.com'
    imgRE = re.compile('/wp-content/uploads/\d+-2560x1600\.jpg')
    pageNums = range(1,15)
    for i in pageNums:
        f = urllib.urlopen(baseURL+'/page/'+str(i)+'/')
        htmlStr = f.read()
        for m in re.finditer(imgRE, htmlStr):
            matchStr = m.group()
            _,saveAsName = os.path.split(matchStr)
            urllib.urlretrieve(baseURL+matchStr,saveAsName)
        
    
