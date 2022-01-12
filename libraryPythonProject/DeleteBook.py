from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "123456"
mydatabase="libraryPyDb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def deleteBook():
    
    bid = bookInfo1.get()

    if bid == "":
        messagebox.showinfo('Error', "ID empty")
        root.destroy()
        return

    try:
        getBooks = "select id from book"
        cur.execute(getBooks)
        con.commit()
    except ValueError:
        messagebox.showinfo("Error", "Failed to get data from database")
        root.destroy()
        return

    notIn = False

    for x in cur:
        if int(bid) == x[0]:
            notIn = True
            break

    if notIn == False:
        messagebox.showinfo('Error',"ID not found in the database")
        root.destroy()
        return

    deleteSql = "delete from book where id = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Book Deleted Successfully")
    except:
        messagebox.showinfo("Check Book ID")

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")

    
    Canvas1 = Canvas(root)

    Canvas1.config(bg='#8129FE')
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Consolas', 21))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=('Consolas',15))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook, font=('Consolas',15))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy, font=('Consolas',15))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()