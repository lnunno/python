'''
Created on Aug 19, 2013

@author: lnunno
'''
from album_images import save_url, top_album_image_urls,convert_img_dir, artist_image_urls
import os
from lastfm.album_images import latex_include_graphics

def main():
    image_links = top_album_image_urls('GrokThis', '423f4d46b119a24a89e91a7d6f945f9a')
    i = 1
    for link in image_links:
        filename = str(i).zfill(4) + os.path.splitext(link)[1]
        local_path = os.path.join('output',filename)
        save_url(link, local_path)
        i += 1

if __name__ == '__main__':
#     main()
#     convert_img_dir('output/', ['.png','.jpg'], '.ppm','output/ppms')
    #print artist_image_urls('423f4d46b119a24a89e91a7d6f945f9a', 'Cake')
    indir = '/home/lnunno/Dropbox/UNM/Fall13/CS522_Digital_Image_Processing/hw/hw1/images'
    #convert_img_dir(indir, ['.pgm','.ppm'], '.png', indir)
    latex_include_graphics(indir,['.png'])