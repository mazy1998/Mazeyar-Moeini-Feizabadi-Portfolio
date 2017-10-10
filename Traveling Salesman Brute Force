##runs on python 2.7 should run without modules, uses brute force and is highely inefficient. 
from Tkinter import *
import time
import random
import math as m
perms = []

##The number of random points on the grid. Time complexity increases factorialy.
num2=6


dots =""
num5=800
num7= 1000
points= []
xc=[]
yc=[]
tempdistance= []
distances = []
tempperms= []
sumofdistances = []
tempdistance = []
ptop = 0
p1 =0
p2 =0
d1=0
d2=0
bestpath = []
worstpath = []

##makes random points
for z in range(0,num2):    
    x =random.randint(0,num5)
    y= random.randint(0,num5)
    points.append(str(str(x)+','+str(y)))
    xc.append(x)
    yc.append(y)

##finds every distance
for w in range(0,num2):
    for p in range(0,num2):
        tempdistance.append(m.sqrt((xc[p]-xc[w])**2+(yc[p]-yc[w])**2))
    distances.append(w+1)
    distances.append(tempdistance)
    tempdistance= []

##efficeint perms of the different paths from perms.py by David Wright       
for t in range(1,num2+1):
        dots = str(dots)+str(t)
def perm2(lst):
	if len(lst) == 0:
		yield []
	elif len(lst) == 1:
		yield lst
	else:
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in perm2(xs):
				yield [x] + p
data = list(dots)
for p in perm2(data):    
    p.append(p[0])
    perms.append(p)
    
##finds all the different paths including distances
for q in range(0,len(perms)):
    tempperms = perms[q]
    for s in range(0,len(tempperms)-1):
        p1 = int(tempperms[s])
        p2 = int(tempperms[s+1])
        ptop = distances[distances.index(int(tempperms[s]))+1]
        tempdistance.append(ptop[p2-1])
    sumofdistances.append(sum(tempdistance))   
    tempdistance = []       
    
##prints the paths
print "Most Efficient Route",min(sumofdistances),perms[int(sumofdistances.index(min(sumofdistances)))]
print "Most Inefficient Route",max(sumofdistances),perms[int(sumofdistances.index(max(sumofdistances)))]
bestpath=perms[int(sumofdistances.index(min(sumofdistances)))]
worstpath=perms[int(sumofdistances.index(max(sumofdistances)))]

##creates frame        
class MyFrame(Frame):
    def __init__(self):
            Frame.__init__(self)
            self.myCanvas = Canvas(width=num5,height=num5,bg="black")
            self.myCanvas.grid()
            for z in range(0, num2):
                    d1 = int(bestpath[z])
                    d2 = int(bestpath[z+1])                   
                    self.myCanvas.create_line(xc[d1-1],yc[d1-1],xc[d2-1],yc[d2-1],fill="green")
            for h in range(0,num2):
                    d1 = int(worstpath[h])
                    d2 = int(worstpath[h+1])
                    self.myCanvas.create_line(xc[d1-1],yc[d1-1],xc[d2-1],yc[d2-1],fill="red")
            
frame02=MyFrame()
frame02.mainloop()
