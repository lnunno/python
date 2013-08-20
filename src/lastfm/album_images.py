'''
Created on Aug 19, 2013

@author: lnunno
'''
import urllib as ul
from bs4 import BeautifulSoup
import os
import subprocess

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

def convert_img_dir(directory, outext,outdir=''):
    if not outdir:
        outdir = directory
    if not os.path.exists(outdir):
        raise Exception('Output path %s does not exist.' % outdir)
    for f in os.listdir(directory):
        filename, ext = os.path.splitext(f)
        if ext == '.png' or ext == '.jpg':
            filepath = os.path.join(directory, f)
            outpath = os.path.join(outdir, filename + outext)
            command = ['convert', filepath, outpath] 
            subprocess.call(command)
            print 'Converted %s to %s' % (filepath,outpath)
        
def save_url(url, outpath):
    if os.path.split(outpath)[1] == '':
        outpath = os.path.join(outpath, os.path.split(url)[1])
    ul.urlretrieve(url, outpath)
    print 'Saved url to %s' % (os.path.abspath(outpath))
    
