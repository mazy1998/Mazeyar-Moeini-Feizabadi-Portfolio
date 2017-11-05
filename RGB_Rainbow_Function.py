## A simple function that scrolls through the rgb color range and can return an array of 8 bit numbers in hex or decimal.
## It works for all real numbers, best if they remain continuous. Set boolHex to true if you want an array of hex values.

import math

def color_fun(x, boolHex):
    pi = math.pi
    red = int(round(127*math.cos((x*pi)/127)+127))
    blue  = int(round(127*math.cos(((x-167)*pi)/127)+127))
    green = int(round(127*math.cos(((x+167)*pi)/127)+127))
    
    if boolHex is True:
      return [hex(red)[2:],hex(blue)[2:],hex(green)[2:]]
    return [red,blue,green]
