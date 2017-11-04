## This program uses stochastic gradient descent to fit a line to a randomly created set of data resembling a line
## Note graphs in the first quadrant
import random
from tkinter import *
import time


class MyFrame(Frame):
    def __init__(self):
            Frame.__init__(self)

            ##number of points and the size of the window
            numPoints = 600
            
            self.myCanvas = Canvas(width=numPoints,height=numPoints,bg="black")
            self.myCanvas.grid()

            ##starts with a random slopes and intercepts
            deltaB = random.randint(-100,100)/100
            deltaM = random.randint(-100,100)/100

            deltaMB = [deltaM, deltaB ]

            
            ## The function that the program will fit to, change the function for different a data set
            def function(x):
              return (.5*x+250)
            
            ## The list with the tuples(x,function(x)) "+random.randint(-10,10)" to create some distribution
            data = [(i,function(i)+random.randint(-10,10)) for i in range(0,numPoints)]
        
            
            ## graphs data
            for i in data:
               self.myCanvas.create_line(i[0],numPoints-i[1],i[0]+1,numPoints-i[1]+1,fill="green")

            size = len(data)

            ## function to update the graph after the adjustments
            def update():
                canvas_id = self.myCanvas.create_line(0,numPoints-b,numPoints,numPoints-(m*numPoints+b),fill="red")
                self.myCanvas.update()
                time.sleep(.1)
                self.myCanvas.after(10, self.myCanvas.delete, canvas_id)  

            ## gradient decent loop
            for z in range(120):

              ## calculates error in deltaB 
              deltaB += (data[0][1]-(deltaB))*.05

              ## calculates the sum of error then adjusts slope
              for i in range(len(data)):
                x = data[i][0]
                y = data[i][1]
                guess = deltaM*x+deltaB                
                error = y-guess
                deltaM += (1/size)*x*error*.001
                m = deltaM
                b = deltaB
            
              ## update after changing deltaM  
              update()              

            ##final update
            canvas_id = self.myCanvas.create_line(0,numPoints-b,numPoints,numPoints-(m*numPoints+b),fill="red")
            print(m,b)    
            
frame02=MyFrame()
frame02.mainloop()
