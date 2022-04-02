import tkinter as tk

class HandleGUI:
    def __init__(self):
        #Create Tk GUI 
        self.root = tk.Tk()
        self.root.title("TIC TAC TOE") 

        #Define canvas
        self.canvas1 = tk.Canvas(self.root, width = 400, height = 300)
        self.canvas1.configure(bg="black")

        #Variables for size scalling 
        self.buttonh = 7
        self.buttonw = 14
        self.bgcolor = "black"

        #Text label
        #I forgot about row=0, but it does not matter
        self.l1=tk.Label(self.root, text="Sample text", height=3, width=self.buttonw, font=("COMIC SANS MS", 20 ,"bold"),bg="white")
        self.l1.grid(row = 1, column = 0)

        #Create buttons
        self.b1=tk.Button(self.root ,text = "", height = self.buttonh, width = self.buttonw, bg = self.bgcolor, activebackground = "white", fg = "white", font = "Arial 20 bold", command = lambda: self.__clickOnButton(0,0))
        self.b1.grid(row = 2,column = 0)
        self.b2=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(0,1))
        self.b2.grid(row=2,column=1)
        self.b3=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(0,2))
        self.b3.grid(row=2,column=2)
        self.b4=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(1,0))
        self.b4.grid(row=3,column=0)
        self.b5=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(1,1))
        self.b5.grid(row=3,column=1)
        self.b6=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(1,2))
        self.b6.grid(row=3,column=2)
        self.b7=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(2,0))
        self.b7.grid(row=4,column=0)
        self.b8=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(2,1))
        self.b8.grid(row=4,column=1)
        self.b9=tk.Button(self.root ,text="",height=self.buttonh,width=self.buttonw,bg=self.bgcolor,activebackground="white",fg="white",font="Arial 20 bold",command=lambda: self.__clickOnButton(2,2))
        self.b9.grid(row=4,column=2)

        self.root.mainloop()
       
    def __clickOnButton(self, row, column):
        print('Click', self.b1, row, column)
        return

    def inititializeGUI(self):

        return





