'''
Created on Aug 19, 2013

@author: lnunno
'''
import urllib as ul
from bs4 import BeautifulSoup
import os

def get_image_tags(user,api_key,image_size="extralarge"):
    url = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=%s&api_key=%s" % (user,api_key)
    html = ul.urlopen(url).read()
    soup = BeautifulSoup(html)
    image_links = [link.text for link in soup.find_all('image',{'size':image_size})]
    i = 1
    for link in image_links:
        filename = str(i).zfill(4) + '.' + os.path.splitext(link)[1]
        ul.urlretrieve(link, os.path.join('output',filename))
        i += 1
        
    
if __name__ == '__main__':
    get_image_tags('USERNAME','API_KEY')