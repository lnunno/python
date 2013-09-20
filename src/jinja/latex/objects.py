'''
Created on Sep 20, 2013

@author: lnunno
'''

class Figure(object):
    '''
    classdocs
    '''

    def __init__(self,graphics):
        '''
        Constructor
        '''
        self.graphics = graphics
        
class Graphic(object):
    
    def __init__(self,path,caption='',scale=1):
        self.path = path
        self.caption = caption
        self.scale = scale

