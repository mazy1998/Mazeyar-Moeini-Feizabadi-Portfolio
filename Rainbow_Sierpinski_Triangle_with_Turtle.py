## Creates a Sierpinski triangle with some gentile colors.

import turtle
import math
bob = turtle.Turtle()

## sets speed 0 being the fastest
bob.speed(0)

## global vairables for color
global color
global x
x=0
color=[255, 57, 57]


## returns a part of a rainbow
def color_fun(x):
    pi = math.pi
    red = 127*math.cos((x*pi)/127)+127
    blue  = 127*math.cos(((x-167)*pi)/127)+127
    green = 127*math.cos(((x+167)*pi)/127)+127
  
    return [int(round(red)),int(round(blue)),int(round(green))]

## draws a triangle at a certian cordinate
def triangle(x,y,side,fill):
  bob.pu()
  bob.goto(x,y)
  bob.pd()
  if fill:
    bob.color(color_fun((x**2+y**2)**.5))
  else:
    bob.color(0,0,0)
  bob.lt(60)
  for x in range(3):
            bob.fd(side)
            bob.lt(120)
  bob.lt(-60)

## calculates the points to draw for the triangle
def points(x, y, level, length):
    if level==1:
        return([x,length/2])
    else:
        d = points(x, y, level-1, length)
        prev= d       
        list1=[]
        if len(prev)>2:
            delta= prev[0][1]/2
            up = math.sqrt((2*delta)**2-delta**2)
            for w in prev:
                x = w[0]
                y = w[1]            
                list1.append([x,y-delta])
                list1.append([x,y+delta])
                list1.append([x+up,y])
            return(list1)
        else:
            w = prev
            x = w[0]
            y = w[1]  
            return([[x,y/2],[x,y*1.5],[(y/2)*math.sqrt(3),y]])
 
## calls the points and triangle function for each       
def sierpinski(level,length):
    if level==0:
         for x in range(3):
            bob.fd(length)
            bob.lt(120)        

    elif level!=0:
        point = points(0,0, level, length)
        if len(point)>2:
            size = point[0][1]
            for y,x in point:
                ## set to Fasle for no colors
                triangle(x,y,size, True)
        else:
            size = point[1]
            ## set to Fasle for no colors
            triangle(point[1],point[0],point[1], True)
            bob.goto(0,0)
        
        sierpinski(level-1,length) 

## sets the (level,length)    
sierpinski(5,700)  

