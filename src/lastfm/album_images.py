'''
Created on Aug 19, 2013

@author: lnunno
'''
import urllib as ul
from bs4 import BeautifulSoup
import os
import subprocess

class UrlBuilder:
    def __init__(self,domain,path,params=None):
        if not params:
            params = {}
        self.domain = domain
        self.path = path
        self.params = params

    def __str__(self):
        acc = 'http://' + self.domain + '/' + self.path + '?'
        acc += '&'.join(['%s=%s'  % (k,v) for k,v in self.params.iteritems() ])
        return acc

    def build(self):
        return self.__str__()

def quicksoup(url):
    html = ul.urlopen(url).read()
    return BeautifulSoup(html)

def image_links(image_size,soup):
    return [link.text for link in soup.find_all('image', {'size':image_size})]
    
def top_album_image_urls(user, api_key, image_size="extralarge", limit=100):
    url = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=%s&api_key=%s&limit=%d" % (user, api_key, limit)
    soup = quicksoup(url)
    links = image_links(image_size, soup)
    return links

def artist_image_urls(api_key, artist,image_size='extralarge'):
    url ='http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=%s&api_key=%s' % (artist,api_key)
    soup = quicksoup(url)
    links = image_links(image_size, soup)
    return links

def convert_img_dir(directory, inexts, outext,outdir=''):
    if not outdir:
        outdir = directory
    if not os.path.exists(outdir):
        raise Exception('Output path %s does not exist.' % outdir)
    for f in os.listdir(directory):
        filename, ext = os.path.splitext(f)
        if ext in inexts:
            filepath = os.path.join(directory, f)
            outpath = os.path.join(outdir, filename + outext)
            command = ['convert', filepath, outpath] 
            subprocess.call(command)
            print 'Converted %s to %s' % (filepath,outpath)
            
def matlab_include_graphics(directory, inexts,scale=0.5):
    for f in os.listdir(directory):
        _, ext = os.path.splitext(f)
        if ext in inexts:
            filepath = os.path.join(directory, f)
            scaleStr = ''
            if scale:
                scaleStr = '[scale=%.1f]' % scale
            print r'\includegraphics%s{%s}' % (scaleStr,filepath) 
        
def save_url(url, outpath):
    if os.path.split(outpath)[1] == '':
        outpath = os.path.join(outpath, os.path.split(url)[1])
    ul.urlretrieve(url, outpath)
    print 'Saved url to %s' % (os.path.abspath(outpath))
    
