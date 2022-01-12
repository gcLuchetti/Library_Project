from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "123456"
mydatabase="libraryPyDb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books"
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg='#8129FE')
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Consolas', 21))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-5s%-30s%-20s%-20s" % ('ID', 'Title', 'Author', 'Status'), bg='black', fg='white', font=("Consolas", 15)).place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="", bg='black', fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from book"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-7s%-32s%-27s%-15s" % (i[0], i[1], i[2], "Avail" if i[3] == 0 else "Issued"), bg='black', fg='white', font=("Consolas", 12)).place(
                relx=0.07, rely=y)
            y += 0.12
    except:
        messagebox.showinfo("Error", "Failed to fetch files from database")
        root.destroy()
        return
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', font=('Consolas',15), command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18, relheight=0.08)
    
    root.mainloop()