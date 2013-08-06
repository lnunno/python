'''
@author: lnunno
'''
import os
from jinja2 import Environment, FileSystemLoader 

def link(href,caption):
    return {'href':href,'caption':caption} 

def generate_webpages():
    template_dir = 'templates/'
    render_dir = 'renders/'
    env = Environment(loader=FileSystemLoader(template_dir),
                         trim_blocks=True)
    home = {'href':'index.html','caption':"Lucas' Homepage"}
    navigation = [link('aboutme.html', 'About me'),link('courseWork.html','Course Work')]
    base_vars = {'home':home,'navigation':navigation}
    index_template = env.get_template('index.html')
    render_and_save(index_template, base_vars, os.path.join(render_dir,'index.html'))

def render_and_save(template,variables,outfile):
    '''Render a template and save to a file.
    '''
    with open(outfile,'w') as f:
        f.write(template.render(variables))
    
def main():
    generate_webpages()
    
if __name__ == '__main__':
    main()