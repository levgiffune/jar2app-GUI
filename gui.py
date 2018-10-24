try:
    from tkinter import *
    
except ImportError:
    from Tkinter import *
    import Tkconstants, tkFileDialog
    
import os, subprocess

#call command and return output
def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

#append text to label
def append_text(label, text):
    current_value = label.cget("text")
    new_value = current_value + text
    label.config(text=new_value)

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        #setup vars
        self.jar_path = ""
        self.icon_path = ""
        self.jdk_path = ""
        self.icon_selected = -1
        self.jdk_selected = -1
        
        # changing the title of our master widget      
        self.master.title("jar2app GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        #file browser opening functions
        def open_jar_browser():
            self.jar_path = tkFileDialog.askopenfilename(initialdir = "~",title = "Select jar file to turn into app",filetypes = [("jar files","*.jar"),("all files","*.*")])
            jar_path_label.config(text = self.jar_path)
            
    
        def open_icon_browser():
            self.icon_selected *= -1
            if self.icon_selected == 1:
                self.icon_path = tkFileDialog.askopenfilename(initialdir = "~",title = "Select icon file to bundle with your app",filetypes = [("Apple icon files","*.icns"),("all files","*.*")])
                icon_path_label.config(text = self.icon_path)
                if self.icon_path == '':
                    iconCheckbox.deselect()
                    self.icon_selected *= -1
    
        def open_jdk_browser():
            self.jdk_selected *= -1
            if self.jdk_selected == 1:
                self.jdk_path = tkFileDialog.askdirectory(initialdir = "~",title = "Select jdk to bundle")
                jdk_path_label.config(text = self.jdk_path)
                print "h"
                if self.jdk_path == '':
                    jdkCheckbox.deselect()
                    self.jdk_selected *= -1
            
        def make_app():
            here = os.path.dirname(sys.argv[0])
            jar2app_files = os.path.join(here, "jar2app")
            jar2app_executable = os.path.join(jar2app_files, "jar2app.py")
            if self.jar_path:
                cmd = ["python", jar2app_executable]
                if self.icon_path:
                    cmd.extend(['-i', self.icon_path.replace(' ', '\\ ')])
                if self.jdk_path:
                    cmd.extend(['-r', self.icon_path.replace(' ', '\\ ')])
                cmd.extend([self.jar_path.replace(' ', '\\ '), "~/Desktop/"])
                cmd = ' '.join(cmd)
                out = system_call(cmd)
                append_text(jar2app_output_label, ("\n\n" + out))
                
        # creating a buttons and checkboxes
        openButton = Button(self, text="Choose Jar file to bundle", command=open_jar_browser)
        iconCheckbox = Checkbutton(self, text="Use Custom icon file (*.icns)", command=open_icon_browser)
        jdkCheckbox = Checkbutton(self, text="Bundle your own jdk (must be directory)", command=open_jdk_browser)
        buildButton = Button(self, text="Bundle App", command=make_app)
        
        #paths of bundled files
        jar_path_label = Label(self, text="")
        icon_path_label = Label(self, text="")
        jdk_path_label = Label(self, text="")
        
        #output of jar2app
        jar2app_output_label=Label(self, text="")
        
        
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
root.geometry("1000x500")

app = Window(root)
root.mainloop()  

