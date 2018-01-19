# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# Specail thanks to Sentdex for his SeaofBTC tutorial
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import math

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename


LARGE_FONT= ("Verdana", 12)

f = Figure(figsize=(11,6), dpi=100)
a = f.add_subplot(111)
  
#labels the axes in the option menu
def menuSet(newvalues):
    
    m = w.children['menu']
    m.delete(0,END)
    for val in newvalues:
        m.add_command(label=val,command=lambda v=variable,l=val:v.set(l))
    variable.set(newvalues[0])
    d = w1.children['menu']
    d.delete(0,END)
    for val1 in newvalues:
        d.add_command(label=val1,command=lambda v=variable1,l=val1:v.set(l))
    variable1.set(newvalues[1])
    
#Opens file dir with pandas
def OpenFile(canvas,w,w1):
    global df,dfnames,name
    name = askopenfilename(
                           filetypes =(("Comma seperated value", "*.csv"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    df = pd.read_csv(name) 
    df = df.dropna(axis=0, how='any')
    dfnames = df.columns.get_values().tolist()
    menuSet(dfnames)
    graphing(canvas,0,name)

#Makes scatter plot, fits line     
def graphing(canvas,r2,name):
    global X1,y_plot,dfnames,names,model
    a.clear()
    npArray = np.array(df)
    
    index = dfnames.index(variable.get())
    index1 = dfnames.index(variable1.get())
    
    X, Y = npArray[:,index], npArray[:,index1]
    maxValue = max(X)
    minValue = min(X)
    xFit = X.reshape(-1, 1)
    yFit = Y.reshape(-1, 1) 
    a.scatter(X,Y, color='blue')
    model = make_pipeline(PolynomialFeatures(int(r2)), Ridge())
    model.fit(xFit,yFit)
    score = model.score(xFit,Y)
    print(score,r2)   
    if name!=None:
        equation.set(makeEquation(model.steps[1][1].coef_, model.steps[1][1].intercept_))
        
    X1 = np.linspace(minValue, maxValue, int(len(X)+200))
    xPredict = X1.reshape(-1, 1)
    y_plot = model.predict(xPredict)    
    a.axis()
    a.set_title(name[name.rfind("/")+1:name.rfind(".")].title())
    a.set_xlabel(variable.get().title())
    a.set_ylabel(variable1.get().title())
    canvas.show()
    
#shows fit line    
def showline(canvas,r2=.93):
    a.clear()  
    graphing(canvas,r2,name)    
    a.plot(X1, y_plot, color="red")
    canvas.show()

#makes expanded equation from array of coefficients/intercept
def makeEquation(coefs, ints):
    coefs = coefs[0][::-1]
    coefs = coefs[:-1]
    final = []
    final1 = ""
    for x in range(len(coefs)):
        final.append(str(str(round(coefs[x],1))+"*X ^ "+str(len(coefs)-x)))
    final.append(str(round(ints[0],2)))
    final1 += final[0]
    for d in final:
        if d != final[0]:
            if d[0].isdigit():
                final1 += (" + "+d)
        
            else:
                final1 += (" - "+d[1:])             
                
             
    return final1

#Object that is the window using tkinter
class LinearRegression(tk.Tk):

    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Regression")       
        container = tk.Frame(self)
        container.grid(row=1,column=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)        
        self.frames = {}

        for F in (StartPage, GraphPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#object that is the startpage        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(row=0)
        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(GraphPage))
        button3.grid(row=2)
        
#object that is the graph page        
class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().grid(row=0, column=0)
        canvas.show()
        
        tool = tk.Frame(self)
        toolbar = NavigationToolbar2TkAgg(canvas, tool)        
        canvas._tkcanvas.grid(row=0, column=0)
        toolbar.update()
        tool.grid(row=2,column=0, stick = "WS")      
        global buttons,w,w1,variable,variable1,equation
        buttons = tk.Frame(self)
        button2 = ttk.Button(buttons, text="Graph Regression Line", 
                            command=lambda: showline(canvas,r2.get()))
        button2.grid(row=0, column=1)
     
        
        button3 = ttk.Button(buttons, text="    Choose File    ",
                            command=lambda : OpenFile(canvas,w,w1))
        button3.grid(row=1, column=1)      
        scalevar = tk.IntVar()
        scalevar.set(1)
        
        equation = tk.StringVar()
        equation.set("Equation")
        labele = tk.Label(self, textvariable = equation)      
        r2 = Scale(buttons, from_=0, to=10,length=200,orient= HORIZONTAL, variable=scalevar)
        r2.grid(row=3,column=1, stick = "N")        
        
        labelp = tk.Label(buttons, text="Max Polynomial")
        labelp.grid(row=2,column=1, stick = "N")        
        labele.grid(row=2,column=0, stick = "eS")      
        label = tk.Label(buttons, text="X Axis", font=LARGE_FONT)  
        
        variable = StringVar(buttons)
        variable.set("X Axis") # default value
        w = OptionMenu(buttons, variable,*["X Axis","Y Axis"])
        w.grid(row=0,column=3)        
        label.grid(row=0,column=2)        
        label2 = tk.Label(buttons, text="Y Axis", font=LARGE_FONT)  
        
        variable1 = StringVar(buttons)
        variable1.set("Y Axis") # default value
        w1 = OptionMenu(buttons, variable1,*["X Axis","Y Axis"])
        w1.grid(row=1,column=3)
        label2.grid(row=1,column=2)        
        buttons.grid(row=0,column=1, sticky="NE")  
        
              
app = LinearRegression()
app.mainloop()
