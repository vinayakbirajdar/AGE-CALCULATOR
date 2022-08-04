# creating a window 
from tkinter import*
from datetime import datetime
root=Tk()
root.title("AGE CALCULATOR")
root.geometry('800x600')
root.resizable(False,False)
# Defining the function 
def age():
    if entry.get():
        current_year = datetime.now().year
        your_age=current_year - int(entry.get())
        vs_1 = Label(f1,text =("Your current age is :",your_age),
                     font=("comicsansms","30"),fg="white")
        vs_1.pack()
        
    else:
        vs_2 = Label(f1,text =("please entre your birth of date!"),
                     font=("comicsansms","30"),fg="white")
        vs_2.pack()
#creating the frame 
f1 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='200')
f1.pack(fill="y",side="bottom")

f2 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='200')
f2.pack(fill="y",side="left")

f4 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='200')
f4.pack(fill="x",side="top")

f3 = Frame(root,borderwidth=3,bg="gray",relief="groove",width='200')
f3.pack(fill="y",side="right")
#Inserting the photo
photo=PhotoImage(file="//Users//vinayakbirajdar//Desktop//image//icon.png")
p_1=Label(image=photo)
p_1.pack()
#Creating the text
Label(text="ENTRE YOUR AGE = ",font=("comicsansms","20"),
      fg="white").place(x=120,y=350)
#taking input
entry=Entry(root,width=20,bd=3,font=20)
entry.place(x=300,y=350)
#creating a button
b_1=Button(root,text="calculate age",font=("comicsansms","30"),fg="black",bg="gray",
          relief=GROOVE,command=age).place(x=100,y=400)
#Desining the frame
vb_2=Label(f2,text="*****",fg='white')
vb_2.pack()

vb_3=Label(f3,text="*****",fg='white')
vb_3.pack()

vb_4=Label(f4,text="created by vinayak birajdar sy-03",fg='white',font=("comicsansms","20"))
vb_4.pack()

root.mainloop()
