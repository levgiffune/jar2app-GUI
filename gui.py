try:
    from tkinter import *
    
except ImportError:
    from Tkinter import *
    import Tkconstants, tkFileDialog
    
import os

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        self.jar_path = ""
        # changing the title of our master widget      
        self.master.title("jar2app GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        #paths of bundled files
        jar_path_label = Label(self, text="")
        
        #output of jar2app
        jar2app_output_label=Label(self, text="OUTPUT")
        
        #place labels
        jar2app_output_label.place(x=50, y=300)
        jar_path_label.place(x=250, y=50)
        
        #file browser opening functions
        def open_jar_browser():
            self.jar_path = tkFileDialog.askopenfilename(initialdir = "~",title = "Select jar file to turn into app",filetypes = (("jar files","*.jar"),("all files","*.*")))
            jar_path_label.config(text = self.jar_path)
            
    
        def open_icon_browser():
            self.icon_path = tkFileDialog.askopenfilename(initialdir = "~",title = "Select jar file to turn into app",filetypes = (("jar files","*.jar"),("all files","*.*")))
            
    
        def open_jdk_browser():
            self.jdk_path = tkFileDialog.askopenfilename(initialdir = "~",title = "Select jar file to turn into app",filetypes = (("jar files","*.jar"),("all files","*.*")))
            
        def make_app():
            here = os.path.dirname(sys.argv[0])
            jar2app_files = os.path.join(here, "jar2app")
            jar2app_executable = os.path.join(jar2app_files, "jar2app.py")
            jar2app = os.popen("python " + jar2app_executable + " " + self.jar_path)
            jar2app_output_label.config(text = "DONE")
            jar2app.close()


        # creating a button instances
        openButton = Button(self, text="Choose Jar file to bundle", command=open_jar_browser)
        iconButton = Button(self, text="Choose icon file to bundle", command=open_icon_browser)
        jdkButton = Button(self, text="Choose jdk (flder or zip) to bundle", command=open_jdk_browser)
        buildButton = Button(self, text="Bundle App", command=make_app)
        
        # placing the button on my window
        openButton.place(x=50, y=50)
        iconButton.place(x=50, y=100)
        jdkButton.place(x=50, y=150)
        buildButton.place(x=50, y=250)


root = Tk()

#size of the window
root.geometry("1000x500")

app = Window(root)
root.mainloop()  

