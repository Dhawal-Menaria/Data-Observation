from tkinter import *
root = Tk()
root.title('Data-Observation-System by Dhawal Menaria')
root.geometry('1000x800')
root.resizable(False,False)

# Nav bar -------------------------------------
bgonav = Canvas(root,width=1000,height=100,border=-10,bg="red")
bgonav.place(x=50,y=20)
logoimg = PhotoImage(file='school_logo.png')
logo = Label(root,image=logoimg,border=0)
logo.place(x=0,y=0)



root.mainloop()