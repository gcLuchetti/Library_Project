from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "123456"
mydatabase="libraryPyDb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

issueTable = "books_issued" 
bookTable = "books"

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()

    if bid == "":
        messagebox.showinfo('Error', "ID empty")
        root.destroy()
        return

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()

    try:
        getBooks = "select id, status from book"
        cur.execute(getBooks)
        con.commit()
    except ValueError:
        messagebox.showinfo("Error", "Failed to get data from database")
        root.destroy()
        return

    notIn = False

    try:
        for x in cur:
            if int(bid) == x[0]:
                notIn = True
                if x[1] == 1:
                    messagebox.showinfo('Error', "The book wasn't avail")
                    root.destroy()
                    return
                break
    except ValueError:
        messagebox.showinfo('Error', "Invalid value")
        root.destroy()
        return

    if notIn == False:
        messagebox.showinfo('Error', "ID not found in the database")
        root.destroy()
        return

    updateStatus = "update book set status = 1 where id = '" + bid + "'"
    try:
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success', "Book issued successfully")
    except:
        messagebox.showinfo("Error", "Error to update data in the database")

    root.destroy()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#8129FE")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Consolas',21))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=("Consolas", 15))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue, font=('Consolas',15))
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy, font=('Consolas',15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()