'''
Created on Sep 20, 2013

@author: lnunno
'''
import os
from jinja2 import Environment, FileSystemLoader 
import jinja.utils.utils as utils

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
    variables = {'package_list':package_list}
    utils.render_and_save(template, variables, os.path.join('renders','base.tex'))
    