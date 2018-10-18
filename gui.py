try:
    from tkinter import *
    
except ImportError:
    from Tkinter import *
    import Tkconstants, tkFileDialog

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("jar2app GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        
        # creating a button instance
        openButton = Button(self, text="Choose File", command=open_file_browser)
        
        # placing the button on my window
        openButton.place(x=50, y=50)


root = Tk()

def open_file_browser():
    root.filename = tkFileDialog.askopenfilename(initialdir = "~",title = "Select jar file to turn into app",filetypes = (("jar files","*.jar"),("all files","*.*")))
    print root.filename

#size of the window
root.geometry("200x200")

app = Window(root)
root.mainloop()  

