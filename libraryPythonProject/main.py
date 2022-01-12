from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

mypass = "123456"
mydatabase="libraryPyDb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("--- Library ---")
root.minsize(width=400,height=400)
root.geometry("600x600")

same = True
n = 0.25

background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

image = ImageTk.PhotoImage(file = "C:/Users/gustavol/OneDrive - AMDOCS/Backup Folders/Desktop/libraryPythonProject/lib.jpg")

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image=image)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Fri Library", bg='black', fg='white', font=('Consolas',16))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add a new book",bg='black', fg='white', font=('Consolas',16), command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete book",bg='black', fg='white', font=('Consolas',16), command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="List all book's",bg='black', fg='white', font=('Consolas',16), command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue book",bg='black', fg='white', font=('Consolas',16), command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return book",bg='black', fg='white', font=('Consolas',16), command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
