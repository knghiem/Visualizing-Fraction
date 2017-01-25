#domino.py
#Jessy Quint and Khanh Nghiem
#Final Project
#December 14,2016
#This program generates a domino-like image to represent the user-inputted fraction.
#The program will also take in mouse clicks that cause the domino pips to change color.

from graphics import *
from buttonclass import *

def drawCover(gwin):
    """Drawing the covers to avoid overlay"""
    cover=Rectangle(Point(5-1.25,6.7-1.25),Point(8+1.25,6.7+1.25))
    cover.draw(gwin)
    cover.setFill("white")
    cover.setOutline("white")

    cover2=Rectangle(Point(5-1.25,2.5-1.25),Point(8+1.25,2.5+1.5))
    cover2.draw(gwin)
    cover2.setFill("white")
    cover2.setOutline("white")

def __inputBox(gwin,height):
    """ __inputBox(gwin,height) is a hidden construction method
    that creates an input box"""        
    inputBox=Entry(Point(2,height),2)
    inputBox.setSize(60)
    inputBox.setFill("white")
    inputBox.draw(gwin)
    return inputBox

def inputBox(gwin):
    """ inputBox(gwin) calls the hidden constructor
    method so that we can create two input boxes in the same step """
    numInputBox = __inputBox(gwin,6.7)
    denInputBox = __inputBox(gwin,2.7)
    return numInputBox,denInputBox

class Dot:
    """ DieView is a widget that displays a graphical
    representation of a standard six-sided die."""
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = DieView(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size   # radius of each pip
        hsize = size / 2.0        # half of size
        offset = 0.6 * hsize      # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)

        # Create 7 circles for standard pip locations
        self.pips = [ self.__makePip(cx-offset, cy-offset), #bottom-left 0
                      self.__makePip(cx-offset, cy), #middle-left 1
                      self.__makePip(cx-offset, cy+offset), #top-left 2
                      self.__makePip(cx, cy), #center 3
                      self.__makePip(cx+offset, cy-offset), #bottom-right 4
                      self.__makePip(cx+offset, cy), #middle-right 5
                      self.__makePip(cx+offset, cy+offset), #top-right 6

                      self.__makePip(cx,cy+offset), #top-middle 7
                      self.__makePip(cx,cy-offset)] #bottom-middle 8

        # Create a table for which pips are on for each value
        # note: 10 will be created by two 5s
        self.onTable = [ [], [3], [1,5], [7,4,0], 
            [0,2,4,6], [0,2,3,4,6], [2,7,6,0,8,4], [2,7,6,0,8,4,3], [0,1,2,4,5,6,7,8], [0,1,2,3,4,5,6,7,8] ]

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip


    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
            

class ColorDot(Dot): #subclass of the superclass 'DieView'

    def setColor(self, color): #method to change color of pips on die drawn
        self.foreground = color #setValue() in DieView uses self.foreground
                                #to set pip color and in this line we set that color

def domino(win):

    #buttons
    visualize=Button(win,1,2,Point(5,9),"Visualize","misty rose")
    quitButton=Button(win,0.5,0.5,Point(9.5,9.5),"X","light gray")

    #draw input boxes to get the fraction
    numInput,denInput=inputBox(win)
    
    fracText=Text(Point(2,5.5),"__")
    fracText.draw(win)
    fracText.setSize(60)
    
    pt=win.getMouse()
    error = None
    
    #while not quit
    while not quitButton.isClicked(pt):
        if visualize.isClicked(pt):
            drawCover(win)
            if error:
                error.undraw()
            try:
                #draw input boxes
                num,den=int(numInput.getText()),int(denInput.getText())

                if num not in [1,2,3,4,5,6,7,8,9,10] or den not in [1,2,3,4,5,6,7,8,9,10]:
                    kill=10/0 #this will create an error and jump to the except line
                
                #create boolean flags to later change pip color
                twoNum = False
                twoDen = False

                #draw pips according to input values
                if num==10:
                    Ndot1 = ColorDot(win, Point(5.8,6.7), 2.5)
                    Ndot1.setColor("dark blue")
                    Ndot1.setValue(5)
                    Ndot2 = ColorDot(win, Point(8,6.7), 2.5)
                    Ndot2.setColor("dark blue")
                    Ndot2.setValue(5)
                    twoNum = True
                else:
                    numDots = ColorDot(win, Point(7,6.7), 2.5)
                    numDots.setColor("dark blue")
                    numDots.setValue(num)
                    
                if den==10:
                    Ddot1 = ColorDot(win, Point(5.8,2.5), 2.5)
                    Ddot1.setColor("dark blue")
                    Ddot1.setValue(5)
                    Ddot2 = ColorDot(win, Point(8,2.5), 2.5)
                    Ddot2.setColor("dark blue")
                    Ddot2.setValue(5)
                    twoDen = True
                else:    
                    denDots = ColorDot(win, Point(7,3), 2.5)
                    denDots.setColor("dark blue")
                    denDots.setValue(den)
                
                dotFrac=Text(Point(7,5.5),"_____")
                dotFrac.draw(win)
                dotFrac.setSize(60)
            except:
                error=Text(Point(5,1),"Please enter whole numbers smaller than 11")
                error.draw(win)
            
        elif not visualize.isClicked(pt): #if a new click was made and it was not on quit button
            try:
                col = color_rgb(randrange(0,220),randrange(0,220),randrange(0,220))
                #change pip colors
                if twoNum:
                    Ndot1.setColor(col)
                    Ndot1.setValue(5)
                    Ndot2.setColor(col)
                    Ndot2.setValue(5)
                else:
                    numDots.setColor(col)
                    numDots.setValue(num)
                    
                if twoDen:
                    Ddot1.setColor(col)
                    Ddot1.setValue(5)
                    Ddot2.setColor(col)
                    Ddot2.setValue(5)
                else:
                    denDots.setColor(col)
                    denDots.setValue(den)
            except:
                print("")
                
        pt=win.getMouse()
    win.close()

