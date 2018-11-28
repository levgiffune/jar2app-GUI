#------------------------------------------------------------------------------
# imports
#------------------------------------------------------------------------------

#python3
try:
    from tkinter import *
    
except ImportError:
    #python2
    from Tkinter import *
    import Tkconstants, tkFileDialog
    
import os, sys

from jar2app.jar2app import make_app

#------------------------------------------------------------------------------
# global variables
#------------------------------------------------------------------------------

jar_path = ""
icon_path = ""
jdk_path = ""
icon_selected = -1
jdk_selected = -1

#------------------------------------------------------------------------------
# utility functions and classes for getting jar2app output
#------------------------------------------------------------------------------

#append text to Tkinter label
def append_text(label, text):
    current_value = label.cget("text")
    new_value = current_value + text
    label.config(text=new_value)
    
class Output:
    def __init__(self):
        self.content = []
    def write(self, string):
        self.content.append(string)

#------------------------------------------------------------------------------
# file browser opening functions
#------------------------------------------------------------------------------

def open_jar_browser(label):
    global jar_path
    path = tkFileDialog.askopenfilename(initialdir = "~", title = "Select icon file to bundle with your app", filetypes = [("jar files","*.jar"),("all files","*.*")])
    jar_path = path
    label.config(text = jar_path)

def open_icon_browser(cbox, label):
    global icon_path, icon_selected
    icon_path = tkFileDialog.askopenfilename(initialdir = "~", title = "Select icon file to bundle with your app", filetypes = [("Apple icon files","*.icns"),("all files","*.*")])
    label.config(text = icon_path)
    if icon_path == '':
        cbox.deselect()

def open_jdk_browser(cbox, label):
    global jdk_path, jdk_selected
    jdk_path = tkFileDialog.askdirectory(initialdir = "~",title = "choose jdk folder")
    label.config(text = jdk_path)
    if jdk_path == '':
        cbox.deselect()

#------------------------------------------------------------------------------
# invoke jar2app and print output for user
#------------------------------------------------------------------------------

def invoke_jar2app(jar_file, output, icon, jdk, label):
    if jar_file:
        out = Output()
        sys.stdout = out
        make_app(jar_file, output=output, icon=icon, jdk=jdk)
        sys.stdout = sys.__stdout__
        output = ''.join(out.content)
        append_text(label, output)

#------------------------------------------------------------------------------
# master GUI widget
#------------------------------------------------------------------------------

class Window(Frame):
    global jar_path, icon_path, jdk_path
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master  
        self.master.title("jar2app GUI")
        self.pack(fill=BOTH, expand=1)
        
        #paths of bundled files
        jar_path_label = Label(self, text="")
        icon_path_label = Label(self, text="")
        jdk_path_label = Label(self, text="")
        
        #output of jar2app
        jar2app_output_label=Label(self, text="Jar2App Output:\n")
        
        # creating a buttons and checkboxes
        openButton = Button(self, text="Choose Jar file to bundle")
        openButton.config(command = lambda: open_jar_browser(jar_path_label))
        iconCheckbox = Checkbutton(self, text="Use Custom icon file (*.icns)")
        iconCheckbox.config(command = lambda: open_icon_browser(iconCheckbox, icon_path_label))
        jdkCheckbox = Checkbutton(self, text="Bundle your own jdk (must be directory)")
        jdkCheckbox.config(command = lambda: open_jdk_browser(jdkCheckbox, jdk_path_label))
        buildButton = Button(self, text="Bundle App", command = lambda: invoke_jar2app(jar_path, "/Users/levgiffune/Desktop/", icon_path, jdk_path, jar2app_output_label))
        
        #place labels and buttons
        jar2app_output_label.place(x=50, y=300)
        jar_path_label.place(x=300, y=50)
        icon_path_label.place(x=300, y=100)
        jdk_path_label.place(x=350, y=150)
        openButton.place(x=50, y=50)
        iconCheckbox.place(x=50, y=100)
        jdkCheckbox.place(x=50, y=150)
        buildButton.place(x=50, y=250)

root = Tk()

#size of the window
root.geometry("1000x700")

app = Window(root)
root.mainloop()  

