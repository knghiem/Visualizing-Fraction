from graphics import *
from math import *
from time import *
from turtle import *
from buttonclass import *
from random import *

def __inputBox(gwin,height):
    """ __inputBox(gwin,height) is a hidden construction method
    that creates an input box"""        

    inputBox=Entry(Point(225,height),2)
    inputBox.setSize(60)
    inputBox.setFill("white")
    inputBox.draw(gwin)
    return inputBox

def inputBox(gwin):
    """ inputBox(gwin) calls the hidden constructor
    method so that we can create two input boxes in the same step """
    numInputBox = __inputBox(gwin,425)
    denInputBox = __inputBox(gwin,575)
    return numInputBox,denInputBox

class DancingPoint():
    def __init__(self,pointA,pointB,r,num,den,scale,sleeptime): #num is short for numerator
        #All points are tuples of x and y not objects
        #Later we'll access the tuples to get x and y to draw point objects
        self.num=num
        self.den=den
        self.pointA=pointA
        self.pointB=pointB
        self.pointAs=[pointA] #start each list that holds tuples with the starting points
        self.pointBs=[pointB]
        self.pointCs=[]
        self.maxrad=-pi*1/(8*scale) #the biggest movement (in radians) that we can make
        self.r=r #radius
        self.scale=scale #scaling the number of points according to user input to prevent too few or too many points
        self.sleeptime=sleeptime #sleeptime will change to prevent drawing too slow or too fast
        self.DPList=[] #this list will hold the Point objects corresponding to the Point C tuples

    def createPoint(self):
        """ this method will create all the points needed as tuples"""
        #radA and radB adjust the unit movement on circle A, cirle B 
        self.radA=self.maxrad/self.den
        self.radB=self.maxrad/self.num

        """DXA,DYA and DXB,DYB are lists of all unit movements to finish one cycle around the circumference of circle A, circle B in pixels
        these values are returned from the hidden method __createPoint
        multiply DXA,DYA,DXB,DYB by both num and den values so that loops are completed with the same number of movements"""
        
        self.DXA,self.DYA=self.__createPoint(self.den,self.pointAs,self.radA)
        self.DXA=self.DXA*self.den*self.num #multiply by den completes 1 cycle, then multiply by num to return to the starting point
        self.DYA=self.DYA*self.num*self.den #multiply by num completes 1 cycle, then multiply by den to return to the starting point
        
        self.DXB,self.DYB=self.__createPoint(self.num,self.pointBs,self.radB)
        self.DXB=self.DXB*self.den*self.num
        self.DYB=self.DYB*self.num*self.den
        
        self.__createDancingPoint() #create all point Cs

    def __createPoint(self,value,pointList,rad):
        """ __createPoint is the hidden method that actually creates all points on a circle. This method will be called separately for each circle."""
        DX=[]
        DY=[]
        numPoints=16*value*self.scale #number of points on a circle
        for i in range(numPoints):
            pointi=pointList[0] #getting the starting point of the circle
            pointiX=pointi[0]
            pointiY=pointi[1]

            rad1=rad+rad*i-pi*1/2 #how far away point i is from the starting point of the circle

            #dx, dy represent the movement in each direction to get to point i
            dx=(self.r+self.r*sin(rad1))-(self.r+self.r*sin(rad+rad*(i-1)-pi*1/2))
            dy=(self.r*cos(rad1))-(self.r*cos(rad+rad*(i-1)-pi*1/2))

            #adding all movements to two lists, DX, DY
            DX.append(-dx)
            DY.append(-dy)

            #adding point i to the list of all points on a circle
            pointi1X=pointiX-(self.r+self.r*sin(rad1))
            pointi1Y=pointiY-(self.r*cos(rad1))
            pointList.append((pointi1X,pointi1Y))
    
        pointList.pop(0) #delete the starting point because we already have it as the last point of the list

        return DX,DY

    def __createDancingPoint(self):
        """ __createDancingPoint is the hidden method that actually creates all points that create the final pattern"""

        #make sure there exists the same number of pointAs and pointBs to create pointCs of intersection
        self.pointAs=self.pointAs*self.num
        self.pointBs=self.pointBs*self.den
        numPoints=16*self.num*self.den*self.scale
        for i in range (numPoints): #create pointCs by using corresponding pointAs and pointBs
            pointA=self.pointAs[i]
            pointB=self.pointBs[i]
            pointC=(pointB[0],pointA[1]) #pointC is created by taking the y-value of pointA and the x-value of corresponding pointB
            self.pointCs.append(pointC)
        
    
    def draw(self,win):
        """ this method does all the visualization"""

        #draw legs to map intersection
        self.legA=Line(Point(150,225),Point(750,225))
        self.legA.draw(win)
        self.legB=Line(Point(600,600),Point(600,75))
        self.legB.draw(win)
        
        colA = "gray"
        colB = "gray"

        #set counts at start to 0
        countA=0
        countB=0

        #keep track of how many times each circle completes one cycle around the circumference
        self.countAText=Text(Point(225,100),"0")
        self.countAText.draw(win)
        self.countAText.setSize(24)
        
        self.countBText=Text(Point(400,525),"0")
        self.countBText.draw(win)
        self.countBText.setSize(24)

        #do all the drawing
        for i in range (len(self.pointAs)): #can use self.pointBs or self.pointCs bc they are of the same length
            pointi=self.pointAs[i]
            pointiX=pointi[0]
            pointiY=pointi[1]
            pointiDraw=Point(pointiX,pointiY) #draw point A

            self.legA.move(self.DXA[i],self.DYA[i]) #move horizontal line according to point A
            
            line=Line(pointiDraw,Point(225,225)) #draw line from center of circle A to point A
            line.draw(win)
            
            if i!=0 and i % (len(self.pointAs)/self.num) == 0: #if circle A finishes a cycle, change the color
                countA+=1
                self.countAText.setText(countA)
                if colA == "white":
                    colA = "gray"
                else:
                    colA = "white"
            line.setFill(colA)

            #do same for point Bs
            pointi=self.pointBs[i]
            pointiX=pointi[0]
            pointiY=pointi[1]
            pointiDraw=Point(pointiX,pointiY)

            self.legB.move(self.DXB[i],self.DYB[i])
            
            line=Line(pointiDraw,Point(525,525))
            line.draw(win)

            if i!=0 and i % (len(self.pointBs)/self.den) == 0:
                countB+=1
                self.countBText.setText(countB)
                if colB == "white":
                    colB = "gray"
                else:
                    colB = "white"
            line.setFill(colB)

            #do same for points Cs
            pointi=self.pointCs[i]
            pointiX=pointi[0]
            pointiY=pointi[1]
            pointiDraw=Point(pointiX,pointiY)
            pointiDraw.draw(win)
            pointiDraw.setFill("purple")

            #keep track of all Point objects for later uses
            self.DPList.append(pointiDraw)

            #connects the points of the patterns with lines
            if i>0:
                line=Line(self.DPList[i],self.DPList[i-1])
                line.draw(win)
                line.setFill("dark blue")
                
            else: #connect the last point to the first point
                line=Line(self.DPList[i],Point(600,225))
                line.draw(win)
                line.setFill("dark blue")
                
            sleep(self.sleeptime)

        #update counts
        self.countAText.setText(countA+1)
        self.countBText.setText(countB+1)

    def savePicture(self,infile,outfile):
        """ This method allows user to save the pattern they created to an image file"""
        img=Image(Point(0,0),infile) #get the source file to manipulate

        #loop through the list of all point Cs        
        for i in range(len(self.pointCs)-1):
            #get point i
            point1=self.pointCs[i]
            x1=round(point1[0])-375
            y1=round(point1[1])-75

            #get point i+1
            point2=self.pointCs[i+1]
            x2=round(point2[0])-375
            y2=round(point2[1])-75

            #drawing all the points in between point i and point i+1 (using parametric line)
            for i in range(20):
                t=0.05*i
                xp=round(x1+t*(x2-x1))
                yp=round(y1+t*(y2-y1))
                img.setPixel(xp,yp,"darkblue")             

        #connecting the last point to the first point
        point1=self.pointCs[0]
        x1=round(point1[0])-375
        y1=round(point1[1])-75

        point2=self.pointCs[len(self.pointCs)-1]
        x2=round(point2[0])-375
        y2=round(point2[1])-75

        for i in range (50):
            t=0.02*i
            xp=round(x1+t*(x2-x1))
            yp=round(y1+t*(y2-y1))
            img.setPixel(xp,yp,"darkblue") 

        #export the processed image
        img.save(outfile)

    def reset(self,gwin):
        """This method allows for another run. We call this method before starting a new iteration of the program."""
        self.countBText.undraw()
        self.countAText.undraw()
        self.legA.undraw()
        self.legB.undraw()
        coverCirc1=Circle(Point(225,225),75)
        coverCirc1.setFill("white")
        coverCirc1.draw(gwin)
        coverCirc2=Circle(Point(525,525),75)
        coverCirc2.setFill("white")
        coverCirc2.draw(gwin)

    def reset2(self,gwin):
        """This is an alternate version of the reset method. We call this method when user hit reset."""
        self.legA.undraw()
        self.legB.undraw()
        self.legA.draw(gwin)
        self.legB.draw(gwin)
        self.countBText.setText("0")
        self.countAText.setText("0")
        coverCirc1=Circle(Point(225,225),75)
        coverCirc1.setFill("white")
        coverCirc1.draw(gwin)
        coverCirc2=Circle(Point(525,525),75)
        coverCirc2.setFill("white")
        coverCirc2.draw(gwin)
           
def orbit2(win):
    #draw quit button
    quitButton=Button(win,20,20,Point(725,25),"X","light gray")
    
    #before user can run the program, they need to decide whether to save what they create 
    prompt=Text(Point(375,100),"This pattern was created by running this program.\nDo you want to save the pattern that you create as an image file?")
    prompt.draw(win)
    
    yes=Button(win,40,75,Point(300,500),"Yes","lavenderblush")
    no=Button(win,40,75,Point(400,500),"No","lavenderblush")

    example=Image(Point(350,300),"example.gif")
    example.draw(win)

    pt=win.getMouse()

    while not yes.isClicked(pt) and not no.isClicked(pt) and not quitButton.isClicked(pt):
        pt=win.getMouse()
        
    if yes.isClicked(pt):
        saveFile=True
        prompt.undraw()
        yes.undraw()
        no.undraw()
        example.undraw()

    elif no.isClicked(pt):
        saveFile=False
        prompt.undraw()
        yes.undraw()
        no.undraw()
        example.undraw()

    elif quitButton.isClicked(pt):
        win.close()
    if not quitButton.isClicked(pt):
        #drawing all buttons
        startButton=Button(win,40,75,Point(375,60),"Start","lavenderblush")

        #if they don't want to save the pattern, they can reset the program as often as they choose
        if saveFile==False:
            resetButton=Button(win,40,75,Point(375,105),"Reset","lavenderblush")

        #configuring the circles
        r=75
        xA,yA=225,225
        xB,yB=525,525

        #draw circles, starting points, and starting connecting lines
        circleA=Circle(Point(xA,yA),r)
        circleA.draw(win)
        
        circleB=Circle(Point(xB,yB),r)
        circleB.draw(win)
        
        pointA=Point(xA+r,yA)
        pointB=Point(xB+r,yB)

        pointC=Point(xB+r,yA)
        pointC.draw(win)
        
        lineA=Line(pointA,pointC)
        lineA.draw(win)
        lineB=Line(pointB,pointC)
        lineB.draw(win)

        line1=Line(Point(xA,yA),pointA)
        line1.draw(win)
        line2=Line(Point(xB,yB),pointB)
        line2.draw(win)


        #drawing fraction input boxes
        numInput,denInput=inputBox(win)
        fracText=Text(Point(xA,450),"__")
        fracText.draw(win)
        fracText.setSize(60)
        fracText.setStyle("bold")

        #open the history.txt file to see how many times the user have saved images
        file=open("history.txt","r")
        infile=file.read()
        file.close()

        #get the last time they saved an image, increase it by one
        i=infile.index("pattern")
        filenum=infile[i+7]
        filenum=int(filenum)+1

        error = None
        dancingPoint = None #indicates the user hasn't used the program

        #set the canvas and output image file name
        canvas="canvas.gif"
        imgname="pattern"+str(filenum)+".gif"

        #fracList keeps track of the fractions user has inputed in 1 run
        fracList=""
        fractionList=Text(Point(350,650),fracList)
        fractionList.draw(win)

        #while user still run the program
        while not quitButton.isClicked(pt):
            pt=win.getMouse()

            if startButton.isClicked(pt):
                if error: #if there is an error, undraw the error message
                    error.undraw()
                if dancingPoint: #if the user has run the program before, reset  
                    dancingPoint.reset(win)
                try:     
                    num,den=int(numInput.getText()),int(denInput.getText()) #get inputs

                    if num not in [1,2,3,4,5,6,7,8,9,10] or den not in [1,2,3,4,5,6,7,8,9,10]:
                        kill=10/0 #this creates an error, program jumps to the except line

                    #configure the the program accordingly to user inputs 
                    elif num<5 and den<5: #if small numbers
                        scale=2 #more points
                        sleeptime=0.01 #slower movements

                    elif num>5 and den>5: #if big numbers
                        scale=1 #fewer points
                        sleeptime=0 #faster movements

                    else: #if moderate inputs (1 big, 1 small)
                        scale=1 #fewer points
                        sleeptime=0.01 #slower movements

                    lineA.undraw() #undraw the starting connecting lines
                    lineB.undraw()

                    #create an instance of the Dancing Point class
                    dancingPoint=DancingPoint((xA+r,yA),(xB+r,yB),r,num,den,scale,sleeptime)
                    dancingPoint.createPoint()
                    dancingPoint.draw(win)

                    #if user wants to save pattern as an image file, call the .saveimage method
                    if saveFile==True:
                        dancingPoint.savePicture(canvas,imgname) #the first time, use the blank canvas
                        canvas=imgname #then keep using the exported file as the canvas to continue drawing until program ends
                        notice=Text(Point(350,675),"This pattern has been saved as "+imgname)
                        notice.draw(win)

                    #update fraction list
                    fracList=fracList+str(num)+"/"+str(den)+", "
                    fractionList.setText(fracList)
                    
                
                except:
                    error=Text(Point(350,685),"Please enter whole numbers smaller than 10")
                    error.setFill("VioletRed3")
                    error.draw(win)
        
            elif saveFile == False and resetButton.isClicked(pt):
                #cover the pattern
                cover=Rectangle(Point(450,150),Point(602,302))
                cover.setFill("white")
                cover.setOutline("white")
                cover.draw(win)
                
                #call the alternate version of reset
                dancingPoint.reset2(win)
                fracList=""
                fractionList.setText(fracList)
                numInput.setText("")
                denInput.setText("")

        #if the user saved an image file, update the history file        
        if saveFile==True:
            file=open("history.txt","w")
            content="pattern"+str(filenum)+"\n"+fracList+".\n"+infile
            file.write(content)
            file.close()
    
        win.close()
            
