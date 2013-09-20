'''
Created on Sep 20, 2013

@author: lnunno
'''
def render_and_save(template,variables,outfile):
    '''Render a template and save to a file.
    '''
    with open(outfile,'w') as f:
        f.write(template.render(variables))
    print 'Rendered %s to %s' % (template,outfile)