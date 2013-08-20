'''
Created on Aug 19, 2013

@author: lnunno
'''
import urllib as ul
from bs4 import BeautifulSoup
import os

def top_album_image_urls(user,api_key,image_size="extralarge"):
    url = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=%s&api_key=%s" % (user,api_key)
    html = ul.urlopen(url).read()
    soup = BeautifulSoup(html)
    image_links = [link.text for link in soup.find_all('image',{'size':image_size})]
    return image_links
        
def save_url(url,outpath):
    if os.path.split(outpath)[1] == '':
        outpath = os.path.join(outpath,os.path.split(url)[1])
    ul.urlretrieve(url, outpath)
    print 'Saved url to %s' % (os.path.abspath(outpath))