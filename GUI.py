import tkinter as tk
from algorithm import Algorithm

class HandleGUI:
    def __init__(self):
        #Store data
        self.results = [["", "", ""],["", "", ""],["", "", ""]]
        self.iteration = 0
        self.winner = ""
        self.start = 0

        #Flag - we cannot make a move when AI thinks, just in case
        self.AImove = False

        #Create Tk GUI 
        self.root = tk.Tk()
        self.root.title("TIC TAC TOE") 

        #Not resizable
        self.root.resizable(False, False) 

        #Define canvas
        self.canvas1 = tk.Canvas(self.root, width = 400, height = 300)
        self.canvas1.configure(bg="black")

        #Path to images
        self.photoO = tk.PhotoImage(file = './robercik.png')
        self.photoX = tk.PhotoImage(file = './x.png')
        self.background = tk.PhotoImage(file = './black.png')

        #Variables for size scalling 
        self.buttonh = 6
        self.buttonw = 2 * self.buttonh
        self.bgcolor = "black"
        self.toprowh = 2

        #Text label
        #I forgot about row=0, but it does not matter
        self.l1=tk.Label(self.root, text="Your turn\nBlack tiles are buttons", height=self.toprowh, width=2*self.buttonw, font=("COMIC SANS MS", 20 ,"bold"),bg="white")
        self.l1.grid(row = 1, column = 0, columnspan=2)

        self.restart=tk.Button(self.root ,text = "Restart", height = self.toprowh, width = self.buttonw, bg = "red", activebackground = "white", fg = "white", font = "Arial 20 bold", command = lambda: self.__clickOnRestart())
        self.restart.grid(row = 1,column = 2)

        #Create buttons
        self.b1=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(0,0))
        self.b1.grid(row = 2,column = 0)
        self.b2=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(0,1))
        self.b2.grid(row=2,column=1)
        self.b3=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(0,2))
        self.b3.grid(row=2,column=2)
        self.b4=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(1,0))
        self.b4.grid(row=3,column=0)
        self.b5=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(1,1))
        self.b5.grid(row=3,column=1)
        self.b6=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(1,2))
        self.b6.grid(row=3,column=2)
        self.b7=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(2,0))
        self.b7.grid(row=4,column=0)
        self.b8=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(2,1))
        self.b8.grid(row=4,column=1)
        self.b9=tk.Button(self.root, image = self.background, bd=0, command = lambda: self.__clickOnButton(2,2))
        self.b9.grid(row=4,column=2)

    def __clickOnRestart(self):
        self.__resetData()

    def __callAI(self):    
        self.AImove = True
        self.l1["text"] = "Greatest Pole of all\n times is thinking"
        
        #Force update - otherwise image may apper after AI choice (2 at once)
        self.root.update()
        row, column = Algorithm().selectPoint(self.results, self.returnSymbol())
        
        #Basically we simulate the human-clicking, but this time
        #we trigger it in an artificial way
        self.__writeSymbol(row, column)
        
        self.l1["text"] = "Your turn\nBlack tiles are buttons"
        self.AImove = False

        if(self.iteration >= 4):
            self.winner = self.__lookForWinner()
        if(self.winner!=""):
            self.__handleWinner()
            return
        #Force update - otherwise image may not appear
        self.root.update()
        return

    def __clickOnButton(self, row, column):
        #Some safeguards
        if(self.winner!="" or self.AImove or self.results[row][column]!=""):
            return
        #Put symbol on the board
        self.__writeSymbol(row, column)
        #We start iterations from 0, so when we have iter=4, we have 5 symbols on the board
        if(self.iteration >= 4):
            self.winner = self.__lookForWinner()
        if(self.winner!=""):
            self.__handleWinner()
            return
        #We want to make AI move just after our own move, so the game is smooth
        self.__callAI()
        return

    def __handleWinner(self):
        if(self.winner == "Draw"):
            self.l1["text"] = "Draw!"
        elif(self.winner == "O"):
            self.l1["text"] = "Greatest Pole is a winner!"
        else:
            self.l1["text"] = "You are a winner!"
        return

    def __resetData(self):
        #Reset to initial state to play again
        self.results = [["", "", ""],["", "", ""],["", "", ""]]
        self.iteration = 0
        self.winner = ""
        self.b1["image"] = self.background
        self.b2["image"] = self.background
        self.b3["image"] = self.background
        self.b4["image"] = self.background
        self.b5["image"] = self.background
        self.b6["image"] = self.background
        self.b7["image"] = self.background
        self.b8["image"] = self.background
        self.b9["image"] = self.background
        self.l1["text"] = "Your turn\nBlack tiles are buttons"
        self.start = 1 - self.start     #we alternate starting turns
        if(self.start):
            #AI move is 1st
            self.__callAI()
        return

    def __lookForWinner(self):
        winner = self.__lookForWinner2("X")
        if(winner=="X"):
            return "X"
        winner = self.__lookForWinner2("O")
        if(winner=="O"):
            return "O"
        if(self.iteration == 9):
            return "Draw"    
        return ""

    def __lookForWinner2(self, player):
        if( #There are 8 conditions (3x rows, 3x columns, 2x diagonnally)
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

    def returnSymbol(self):
        return "X" if ((self.iteration+self.start)%2 == 0) else "O"

    def __writeSymbol(self, row, column):
        #Check if empty
        if(self.results[row][column]!=""):
            return
        
        self.results[row][column] = self.returnSymbol()

        #Assign proper image to a button
        if (row == 0):
            if(column == 0):               
                self.b1["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            elif (column == 1):
                self.b2["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            else:
                self.b3["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
        elif (row == 1):
            if(column == 0):
                self.b4["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            elif (column == 1):
                self.b5["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            else:
                self.b6["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
        else:
            if(column == 0):
                self.b7["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            elif (column == 1):
                self.b8["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO
            else:
                self.b9["image"] = self.photoX if ((self.iteration+self.start)%2 == 0) else self.photoO

        self.iteration+=1
        return

    def initializeGame(self):  
        self.root.mainloop()
        return





