## Creates a Koch curve/snowflake using recursion and a rainbow function.
import turtle
import math
bob = turtle.Turtle()

## sets speed 0 being the fastest
bob.speed(0)

## global vairables for color
global color
global x
x=0
color=[255, 57,57]
bob.pencolor(255,57,57)

## returns a part of a rainbow
def color_fun(x, boolHex):
    pi = math.pi
    red = int(round(127*math.cos((x*pi)/127)+127))
    blue  = int(round(127*math.cos(((x-167)*pi)/127)+127))
    green = int(round(127*math.cos(((x+167)*pi)/127)+127))
    if boolHex is True:
      return [hex(red)[2:],hex(blue)[2:],hex(green)[2:]]
    return [red,blue,green]

## makes 1/3 of the snowflake
def koch_curve(level, length):
        global color
        global x       
        
        ## notice the 4 recursive calls apply the Koch rule to a single line
        if level!=0:           
            koch_curve(level-1, length/3)
            bob.lt(-60)
            bob.pencolor(color[0],color[1],color[2])
            color = color_fun(x, False)
            x+=1
            
            koch_curve(level-1, length/3)
            bob.lt(120)
            bob.pencolor(color[0],color[1],color[2])
            color = color_fun(x, False)
            x+=1
            
            koch_curve(level-1, length/3)
            bob.lt(-60)
            bob.pencolor(color[0],color[1],color[2])
            color = color_fun(x, False)
            x+=1
            koch_curve(level-1, length/3)
            
        else:            
            bob.fd(length)  
            
## draws 3 of the curves connected        
def koch_snowflake(level, length):
    for x in range(3):
        koch_curve(level,length)
        bob.lt(120)

## sets the (level,length) 
koch_snowflake(4, 525)
