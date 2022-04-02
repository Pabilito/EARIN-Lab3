import tkinter as tk

class HandleGUI:
    def __init__(self):
        #Store data
        self.results = [["", "", ""],["", "", ""],["", "", ""]]
        self.iteration = 0
        self.winner = ""

        #Create Tk GUI 
        self.root = tk.Tk()
        self.root.title("TIC TAC TOE") 

        #Not resizable
        self.root.resizable(False, False) 

        #Define canvas
        self.canvas1 = tk.Canvas(self.root, width = 400, height = 300)
        self.canvas1.configure(bg="black")

        #Variables for size scalling 
        self.buttonh = 6
        self.buttonw = 2 * self.buttonh
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
        self.__writeSymbol(row, column)
        #We start iterations from 0, so when we have iter=4, we have 5 symbols on the board
        if(self.iteration >= 4):
            self.winner = self.__lookForWinner()
        if(self.winner!=""):
            self.__handleWinner()
        return

    def __handleWinner(self):
        print(self.winner)
        return

    def __lookForWinner(self):
        winner = self.__lookForWinner2("X")
        if(winner=="X"):
            return "X"
        winner = self.__lookForWinner2("O")
        if(winner=="O"):
            return "O"    
        return ""

    def __lookForWinner2(self, player):
        if(
        self.results[0][0]==self.results[0][1]==self.results[0][2]==player or 
        self.results[1][0]==self.results[1][1]==self.results[1][2]==player or 
        self.results[2][0]==self.results[2][1]==self.results[2][2]==player or 
        self.results[0][0]==self.results[1][0]==self.results[2][0]==player or 
        self.results[0][1]==self.results[1][1]==self.results[2][1]==player or 
        self.results[0][2]==self.results[1][2]==self.results[2][2]==player or
        self.results[0][0]==self.results[1][1]==self.results[2][2]==player or
        self.results[0][2]==self.results[1][1]==self.results[2][0]==player):
            return player    
        return

    def __writeSymbol(self, row, column):
        #Check if empty
        if(self.results[row][column]!=""):
            return
        
        self.results[row][column] = "X" if (self.iteration%2 == 0) else "O"

        if (row == 0):
            if(column == 0):
                self.b1["text"] = self.results[row][column]
            elif (column == 1):
                self.b2["text"] = self.results[row][column]
            else:
                self.b3["text"] = self.results[row][column]
        elif (row == 1):
            if(column == 0):
                self.b4["text"] = self.results[row][column]
            elif (column == 1):
                self.b5["text"] = self.results[row][column]
            else:
                self.b6["text"] = self.results[row][column]
        else:
            if(column == 0):
                self.b7["text"] = self.results[row][column]
            elif (column == 1):
                self.b8["text"] = self.results[row][column]
            else:
                self.b9["text"] = self.results[row][column]

        self.iteration+=1
        return





