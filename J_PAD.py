from tkinter import *
from tkinter.messagebox import showinfo,askyesnocancel
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from tkinter import simpledialog



def new(event=None):       #.................Creates new file and saves current flle...........#
    global file
    var=askyesnocancel("New..","Do you want to save your document")
    if(var!=None):
        if(var==True):
            saveas()
        if(file!=None):
            root.title("Untitled - J_PAD")
            file=None
            text.delete(1.0,END)

def openfile(event=None):    #.................opens desired file in J_PAD...........#
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
    if file == "":      #.................Checks file exists or not...........#
        file=None
    else:
        root.title(os.path.basename(file)+"-J_PAD")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()


def saveas(event=None):   #.................Saves known file with same name and untitled files with a new name in desired location...........#
    global file
    if file==None:  #.................Checks file is untitled or known...........#
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file =="":   #.................Checks file exists or not...........#
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-J_PAD")
    else:
         f=open(file,"w")     #.................Write to the existing file...........#
         f.write(text.get(1.0,END))
         f.close()
         

def exitroot(event=None):    #.................Exits the main loop...........#
    var=askyesnocancel(title=f"QUIT-{file}",message="Do you want to save the file before exit..")
    if(var!=None):
        if(var==True):
            saveas()
        root.destroy()
    

def copy(event=None):     #.................Handles copy operation in file...........#
    text.event_generate(("<<Copy>>"))

def paste(event=None):    #.................Handles paste operation in file...........#
    text.event_generate(("<<Paste>>"))

def selectall(event=None):  #................Selects all the text in the file...........#
    text.tag_add(SEL,"1.0",END)
    text.mark_set(INSERT,"1.0")
    text.see(INSERT)
    return 'break'

def cut(event=None):        #.................Handles cut operation in file...........#
    text.event_generate(("<<Cut>>"))

def find(event=None):       #.................finds the occurence of given word...........#
    findstr=simpledialog.askstring("Find...","Enter the text you want to search")
    textstr=text.get(1.0,END)
    occurence=textstr.count(findstr)
    showinfo("Find...",f"{findstr} have {occurence} occurences in the text ")

def about(event=None):     #.................about J_PAD...........#
    showinfo("J-PAD","Text editor by Himanshu")

def help(event=None):       #.................Shows important information for help...........#
    showinfo("Help...","For any help mail your queries on gmail devranihimanshu81@gmail.com\nContact on given numbers :- 9548609762    9761594415")

file=None

#.............................Main window layout......................#
root=Tk()                      #...................creates new window...............#
root.wm_iconbitmap("1.ico")
root.title("Untitled-J_PAD")   #..................title of the root............#
root.geometry("1000x800")     #...................defines initial geometry to the root.........# 
scrollbarx=Scrollbar(root)    #....................add scroll bar................#
scrollbarx.pack(side=RIGHT,fill=Y)
text = Text(root,font="comicsansms 11 bold")   #....................text area for editor..........#
text.pack(expand=True,fill=BOTH)
scrollbarx.config(command=text.yview)          #....................fix scroll bar with y view of text area...........#
menubar=Menu(root)     #..............................Menu bar......................#
#.....................file menu......................#
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=new,accelerator="Ctrl+N")
root.bind_all("<Control-N>",new)  #..........binds function with key press.........#
root.bind_all("<Control-n>",new)
filemenu.add_command(label="Open",command=openfile,accelerator="Ctrl+O")
root.bind_all("<Control-o>",openfile)  #..........binds function with key press.........#
root.bind_all("<Control-O>",openfile)
filemenu.add_command(label="Save As",command=saveas,accelerator="Ctrl+S")
root.bind_all("<Control-s>",saveas)  #..........binds function with key press.........#
root.bind_all("<Control-S>",saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exitroot,accelerator="Ctrl+Q")
root.bind_all("<Control-q>",exitroot)  #..........binds function with key press.........#
root.bind_all("<Control-Q>",exitroot)
menubar.add_cascade(label="File",menu=filemenu)


#.....................edit menu......................#
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Copy",command=copy,accelerator="Ctrl+C")
root.bind_all("<Control-C>",copy)  #..........binds function with key press.........#
root.bind_all("<Control-c>",copy)
editmenu.add_command(label="Paste",command=paste,accelerator="Ctrl+V")
root.bind_all("<Control-v>",paste)  #..........binds function with key press.........#
root.bind_all("<Control-V>",paste)
editmenu.add_command(label="Cut",command=cut,accelerator="Ctrl+X")
root.bind_all("<Control-X>",cut)  #..........binds function with key press.........#
root.bind_all("<Control-x>",cut)
editmenu.add_separator()
editmenu.add_command(label="Select All",command=selectall,accelerator="Ctrl+A")
root.bind_all("<Control-A>",selectall)   #..........binds function with key press.........#
root.bind_all("<Control-a>",selectall)
editmenu.add_command(label="Find",command=find,accelerator="Ctrl+F")
root.bind_all("<Control-F>",find)   #..........binds function with key press.........#
root.bind_all("<Control-f>",find)
menubar.add_cascade(label="Edit",menu=editmenu)

#.....................help menu......................#
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=help)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)
root.mainloop()       #..........................starts root.................#