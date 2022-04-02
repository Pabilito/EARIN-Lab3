import tkinter as tk

def clickOnButton(button, row, column):
    print('Click', button, row, column)
    return

#Create Tk GUI 
root = tk.Tk()
root.title("TIC TAC TOE") 

#Define canvas
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.configure(bg="black")

#Variables for size scalling 
buttonh = 7
buttonw = 14
bgcolor = "black"

#Text label
l1=tk.Label(root, text="Sample text", height=3, width=buttonw, font=("COMIC SANS MS", 20 ,"bold"),bg="white")
l1.grid(row = 1, column = 0)

#Create buttons
b1=tk.Button(root ,text = "", height = buttonh, width = buttonw, bg = bgcolor, activebackground = "white", fg = "white", font = "Arial 20 bold", command = lambda: clickOnButton(b1,0,0))
b1.grid(row = 2,column = 0)
b2=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b2,0,1))
b2.grid(row=2,column=1)
b3=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b3,0,2))
b3.grid(row=2,column=2)
b4=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b4,1,0))
b4.grid(row=3,column=0)
b5=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b5,1,1))
b5.grid(row=3,column=1)
b6=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b6,1,2))
b6.grid(row=3,column=2)
b7=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b7,2,0))
b7.grid(row=4,column=0)
b8=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b8,2,1))
b8.grid(row=4,column=1)
b9=tk.Button(root ,text="",height=buttonh,width=buttonw,bg=bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: clickOnButton(b9,2,2))
b9.grid(row=4,column=2)

root.mainloop()

