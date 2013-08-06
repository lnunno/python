'''
Puzzle represented as single list of 9 elements.
Created on Oct 18, 2012

@author: lnunno
'''
import random

SEED = 1337
random.seed(SEED)
BLANK = -99
SOLUTION = [1, 2, 3, 8, -99, 4, 7, 6, 5]

def createRandomPuzzle():
    '''
    Return random 8-puzzle.
    '''
    p = [1, 2, 3, 8, -99, 4, 7, 6, 5]
    random.shuffle(p)
    return p
    
def printPuzzle(p):
    acc = ""
    spaces = 3
    separator = '-'*spaces*3 
    print separator
    for i in range(len(p)):
        if p[i] == BLANK:
            s = 'X'
        else: s = str(p[i])
        if ((i+1) % 3) == 0 and i > 1: 
            acc += s+' '*spaces 
            if i != 8: print acc,'\n'
            else: print acc
            acc = ""
        else: 
            acc += s+' '*spaces 
    print separator
    
def moveUp(p):
    '''
    Error if return val < 0
    else success.
    '''
    blankIndex = p.index(BLANK)
    #Can't move if on the top edge.
    if blankIndex <= 2: return -1
    #Move 
    else: 
        p[blankIndex] = p[blankIndex-3]
        p[blankIndex-3] = BLANK
        return 1
    
def moveDown(p):
    '''
    Error if return val < 0
    else success.
    '''
    blankIndex = p.index(BLANK)
    #Can't move if on the bottom edge.
    if blankIndex >= 6: return -1
    #Move 
    else: 
        p[blankIndex] = p[blankIndex+3]
        p[blankIndex+3] = BLANK
        return 1
    
def moveRight(p):
    '''
    Error if return val < 0
    else success.
    '''
    blankIndex = p.index(BLANK)
    #Can't move if on the right edge.
    if ((blankIndex+1) % 3) == 0: return -1
    #Move 
    else: 
        p[blankIndex] = p[blankIndex+1]
        p[blankIndex+1] = BLANK
        return 1

def moveLeft(p):
    '''
    Error if return val < 0
    else success.
    '''
    blankIndex = p.index(BLANK)
    #Can't move if on the left edge.
    if (blankIndex % 3) == 0: return -1
    #Move 
    else: 
        p[blankIndex] = p[blankIndex-1]
        p[blankIndex-1] = BLANK
        return 1
    
def generateChildren(p):
    '''
    Generate child states from current p state. Up to caller to check for repeat states. 
    Will return less states if some moves not possible from the given state. 
    Pass a copy of current puzzle to ensure original is unmodified. 
    '''
    children = []
    #Save a copy of the current state.
    orig = list(p)
    #Move in every direction. Don't add if error. Restore original p after generating each move.
    if moveUp(p) > 0: children.append(p)
    p = list(orig)
    if moveDown(p) > 0: children.append(p)
    p = list(orig)
    if moveLeft(p) > 0: children.append(p)
    p = list(orig)
    if moveRight(p) > 0: children.append(p)
    p = list(orig)
    return children

def moveAndPrint(direction,p):
    if direction == "Left":
        moveLeft(p)
    elif direction == "Right":
        moveRight(p)
    elif direction == "Up":
        moveUp(p)
    elif direction == "Down":
        moveDown(p)
    print "Moved",direction
    printPuzzle(p)
        
def testMoving():
    p = [1, 2, 3, 8, -99, 4, 7, 6, 5]
    print "Original"
    printPuzzle(p)
    directions = ["Up","Down","Left","Right"]
    #Test moving around a bit.
    for direction in directions:
        for _ in range(3):
            moveAndPrint(direction, p)

def testChildGen(p):
    print "Original"
    printPuzzle(p)
    #Test generating child states.
    i = 0
    children = generateChildren(list(p))
    for child in children:
        print "Child"+str(i)
        printPuzzle(child)
        i+=1
    #Make sure our original is unchanged.
    print "Original2. Same?"
    printPuzzle(p)
    
def isSolved(p):
    '''
    Test if the given puzzle is solved.
    '''
    return (p == SOLUTION)
            
def test():
        #Some nastyness to test the functions.
    testMoving()
    p = [1, 2, 3, 8, -99, 4, 7, 6, 5]
    testChildGen(p)
    #Test generating some random 8-puzzles.
    i = 0
    for i in range(10):
        p = createRandomPuzzle()
        print "Random Puzzle #",str(i)
        printPuzzle(p)
        print "Solved?",str(isSolved(p))
        i+=1
    p = [1, 2, 3, 8, -99, 4, 7, 6, 5]
    print "Solved State:"
    printPuzzle(p)
    print "Solved?",str(isSolved(p))
    
if __name__ == '__main__':
    test()