#fraction.py
#Khanh Nghiem and Jessy Quint
#Fiinal Project
#December 14, 2016

#This module holds main function that runs the entire program by
#importing other modules holding classes and methods necessary
#for computations. This module also draws opening graphics and menu
#used to begin program.
#IMPORTANT NOTE: This program is designed to be run from a PC computer.
#The program could crash if run on a Mac device.

from graphics import *
from buttonclass import *
from orbit2 import *
from domino import *

def __inputBox(gwin,height,word):
    """ __inputBox(gwin,height,word) is a hidden construction method
    that creates an input box with a prompt for the user and draws both
    into a graphic window """        
    prompt=Text(Point(155,height),word)
    prompt.setSize(10)
    prompt.draw(gwin)
    inputBox=Entry(Point(450,height),2)
    inputBox.setSize(60)
    inputBox.setFill("white")
    inputBox.draw(gwin)
    return inputBox

def inputBox(gwin,prt1,prt2):
    """ inputBox(gwin,prompt1,prompt2) calls the hidden constructor
    method so that we can create two input boxes in the same step """
    numInputBox = __inputBox(gwin,300, prt1)
    line=Text(Point(450,345),"____")
    line.draw(gwin)
    line.setSize(40)
    denInputBox = __inputBox(gwin,450, prt2)
    return numInputBox,denInputBox

def main():
    win=GraphWin("Fraction",600,600)
    win.setBackground("white")

    #title
    title=Text(Point(300,70),"Fun with Fractions")
    title.setSize(30)
    title.setFill("midnight blue")
    title.draw(win)

    #add cute cat image objects
    meow=Image(Point(115,70),"meow.png")
    meow.draw(win)
    meow2=Image(Point(485,70),"meow.png")
    meow2.draw(win)

    #draw buttons
    quitButton=Button(win,20,20,Point(565,25),"X","light gray")
    menu=Button(win,30,450,Point(300,150),"MENU","lavender")
    Domino=Button(win,45,200,Point(175,200),"Domino","misty rose")
    Orbit=Button(win,45,200,Point(425,200),"Orbit","LightCyan2")

    #outline boxes
    DpromptBox=Rectangle(Point(20,270),Point(580,330))
    DpromptBox.setOutline("misty rose")
    DpromptBox.setFill("misty rose")
    DpromptBox.draw(win)
    OpromptBox=Rectangle(Point(20,340),Point(580,460))
    OpromptBox.setOutline("LightCyan2")
    OpromptBox.setFill("LightCyan2")
    OpromptBox.draw(win)

    DpromptBox2=Rectangle(Point(23,273),Point(577,327))
    DpromptBox2.setOutline("white")
    DpromptBox2.setFill("white")
    DpromptBox2.draw(win)
    OpromptBox2=Rectangle(Point(23,343),Point(577,457))
    OpromptBox2.setOutline("white")
    OpromptBox2.setFill("white")
    OpromptBox2.draw(win)

    #description text for user
    Dprompt=Text(Point(300,300),"DOMINO will produce a visual representation of an inputted fraction, similar to a domino.\nClick anywhere within the blank space in the window to change the color of the domino.")
    Dprompt.setSize(10)
    Dprompt.draw(win)
    Oprompt=Text(Point(300,400),"ORBIT will create a pattern that represents an inputted fraction or fractions.\nThere will be two circles of the same radius, and a point on each circle (point A, point B)\nmoving along the circumference at relative speeds corresponding to the fraction.\nBy drawing a horizontal line from point A and a vertical line from point B,\nwe trace the intersection point--thus creating a beautiful pattern.")
    Oprompt.setSize(10)
    Oprompt.draw(win)
    
    pt=win.getMouse()
    
    while not quitButton.isClicked(pt):
        if Orbit.isClicked(pt):
            #get text from input boxes
            #create graphic window to display orbit animation
            win2=GraphWin("Orbit",750,750)
            win2.setBackground("white")
            #call orbit funtion from other module to run program
            #and pass in the window, numerator and denominator values to use
            orbit2(win2)
            pt=win.getMouse()


        elif Domino.isClicked(pt):
            #do same as above but call domino() function
            win2 = GraphWin("Domino",450,450)
            win2.setCoords(0,0,10,10)
            win2.setBackground("white")
            domino(win2)
            pt=win.getMouse()
                    
        else:
            pt=win.getMouse()
    win.close()
main()
