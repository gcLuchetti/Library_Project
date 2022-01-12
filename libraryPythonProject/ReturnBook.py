from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "123456"
mydatabase="libraryPyDb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()

    if bid == "":
        messagebox.showinfo('Error', "ID empty")
        root.destroy()
        return

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
                if x[1] == 0:
                    messagebox.showinfo('Error', "The book wasn't issued")
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


    updateStatus = "update book set status = 0 where id = '"+bid+"'"
    try:
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success', "Book returned Successfully")
    except:
        messagebox.showinfo("Error",  "Error to update data in the database")
    
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#8129FE")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Consolas',21))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=("Consolas", 15))
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn, font=('Consolas',15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy, font=('Consolas',15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()