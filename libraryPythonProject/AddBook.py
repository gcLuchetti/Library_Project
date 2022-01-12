from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():

    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    if title == "" or author == "" or status not in ("avail", "issued"):
        messagebox.showinfo("Error", "Missing data.");
        root.destroy()
        return

    title.strip()
    author.strip()

    if status == "avail":
        status = 0
    else:
        status = 1

    insertBooks = "insert into Book(title, author, status) values('"+title+"','"+author+"',"+status.__str__()+");"

    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into database")

    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")

    # Add your own database name and password here to reflect in the code
    mypass = "123456"
    mydatabase="libraryPyDb"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)

    Canvas1.config(bg='#8129FE')
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg='black',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Book", bg='black', fg='white', font=('Consolas', 21))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white', font=('Consolas',12))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=('Consolas',12))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white', font=('Consolas',12))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="Add",bg='#d1ccc0', fg='black', font=('Consolas',15),command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', font=('Consolas',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()