from graphics import *
from random import *

class Button:

    """A rectangular is a labeled rectangle in a window. It is enabled or
disabled with the activate() and deactivated() methods. The isClicked(pt)
method returns True if the button is enabled and pt is inside it."""
    
    #first set up the construtor method
    #this is automatically called each time button class is instantiated

    def __init__(self,win,height,width,centerPt,words,color):
        """Creates a rectangular button, where:
        win is the GraphWin obect where the button will be drawn,
        height is an integer
        width is an integer
        centerPt is a Point object the button will be centered on
        wrds is a string that will appear on the button"""
        
        x,y=centerPt.getX(), centerPt.getY()
        self.xmax=x+width/2
        self.xmin=x-width/2
        self.ymax=y+height/2
        self.ymin=y-height/2
        self.rect=Rectangle(Point(self.xmin,self.ymin),Point(self.xmax,self.ymax))
        self.rect.draw(win)
        self.rect.setFill(color)
        self.rect.setOutline(color)
        self.label=Text(centerPt,words)
        self.label.draw(win)
        self.activate()

    def isClicked(self,pt):
        """returns true if Point p is inside"""
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def activate(self):
        """Sets this button to active."""
        self.active=True
        self.rect.setWidth(2)
        self.label.setFill('black')

    def deactivate(self):
        """Sets this button to inactive mode"""
        self.active=False
        self.rect.setWidth(1)
        self.label.setFill('gray')

    def setLabel(self,newLabel):
        """mutator method"""
        self.label.setText(newLabel)

    def getLabel(self):
        return self.label.getText()

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()
        
def main():
    print("We're in the Button Class")
    win=GraphWin("Dice Roller",200,200)
    rollButton=Button(win,20,120,Point(100,105),"Roll Dice")
    quitButton=Button(win,20,40,Point(100,180),"Quit")
    quitButton.deactivate()

    die1=DieView(win, Point(50,50), 50)
    die2=DieView(win, Point(150,50), 50)
    
    pt=win.getMouse()
    while not rollButton.isClicked(pt):
        pt=win.getMouse()
    
    quitButton.activate()
    value1=randrange(1,7)
    value2=randrange(1,7)
    die1.setValue(value1)
    die2.setValue(value2)

    pt=win.getMouse()
    while not quitButton.isClicked(pt):
        value1=randrange(1,7)
        value2=randrange(1,7)
        die1.setValue(value1)
        die2.setValue(value2)
        pt=win.getMouse()
    win.close()
if __name__=='__main__':
    main() 
    
