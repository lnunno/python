'''
Created on Sep 20, 2013

@author: lnunno
'''
import os
from jinja2 import Environment, FileSystemLoader 
import jinja.utils.utils as utils
from jinja.latex.objects import Figure,Graphic

def generate_graphics(rootdir,scale=1):
    graphics = {}
    for i in os.listdir(rootdir):
        path = os.path.abspath(os.path.join(rootdir,i))
        if os.path.splitext(i)[1] == '.png':
            graphics[i] = Graphic(path,i,scale)
    return graphics
    
if __name__ == '__main__':
    template_dir = 'templates/'
    render_dir = 'renders/'
    env = Environment(loader=FileSystemLoader(template_dir),
                         trim_blocks=True)
    template = env.get_template('base.html')
    package_list = ['verbatim',
                    'graphicx',
                    'listings',
                    'color',
                    'textcomp',
                    'amsmath',
                    'pdfpages']
    base_path = '/home/lnunno/Dropbox/UNM/Fall13/CS522_Digital_Image_Processing/hw/hw2/images/'
    graphics = generate_graphics(base_path,scale=0.5)
    figure_list = [
                   Figure([graphics.get(x) for x in ["filledHoles.png",'noSquarePads.png','squarePadsOverlay.png'] ]),
                   Figure([graphics.get(x) for x in ['pcb2.png',"bigHoleOverlay.png","smallHolesOverlay.png"] ]),
                   Figure([graphics.get(x) for x in ['noLargeCircularPads.png',"smallCircularPadsOverlay.png","largeCircularPadsOverlay.png"] ]),
                   Figure([graphics.get(x) for x in ['pcb2.png','nopads.png','wiresOverlay.png'] ]),
                   Figure([graphics.get('pcb2.png'),graphics.get('pcb2Overlays.png')])
                   ]
    variables = {'package_list':package_list,'figure_list':figure_list}
    utils.render_and_save(template, variables, os.path.join('renders','base.tex'))
    