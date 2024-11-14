import tkinter as tk
import random

class Minesweeper: 

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Minesweeper")

        self.label = tk.Label(self.root, text="Minesweeper", font=('Arial', 22))
        self.label.pack()

        self.label2 = tk.Label(self.root, text="How large of a map? (min 5, max 20)", font=('Arial', 12))
        self.label2.pack(pady=10)

        self.entry = tk.Entry(self.root, font=('Arial', 12))
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Enter", font=('Arial', 12), command=self.enter)
        self.button.pack(pady=10)

        self.root.mainloop()

    def enter(self):
        try:
            gridSize = int(self.entry.get())
            if 5 <= gridSize <= 20:
                self.root.destroy()
                Game(gridSize)
            else:
                self.label2.config(text="Please enter a number between 5 and 20")
        except ValueError:
            self.label2.config(text="Please enter a valid number")

class Game: 
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.bombMap = [[0 for _ in range(gridSize)] for _ in range(gridSize)]
        self.numMap = [[0 for _ in range(gridSize)] for _ in range(gridSize)]
        self.nameMap = [[" " for _ in range(gridSize)] for _ in range(gridSize)]
        self.place_bombs()
        self.calculate_numbers()

        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Minesweeper")

       
    
        self.buttons = []
        for x in range(gridSize):
            pos = 0
            row = []
            for y in range(gridSize):
                text = '*' if self.bombMap[x][y] == 1 else str(self.numMap[x][y])
                button = tk.Button(self.root, text=" ", font=('Arial', 12), width=3, height=1,state= "active", command= lambda x=x, y=y:self.update_button(x,y))
                button.text = text
                button.grid(row=x, column=y)
                row.append(button)
                pos = pos + 1
            self.buttons.append(row)
            pos = pos + 1

        self.root.mainloop()
        
    
    def update_button(self, x, y):
        self.buttons[x][y].config(text = self.buttons[x][y].text, state = "disabled")
        if self.numMap[x][y] == 0:
            self.showAll(x,y)

    def showAll(self,x,y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if  0 <= nx < self.gridSize and 0 <= ny < self.gridSize and self.buttons[nx][ny]["text"] == " " and self.bombMap[nx][ny] == 0:
                self.update_button(nx,ny)



    

    def place_bombs(self):
        num_bombs = max(5, self.gridSize * self.gridSize // 10)
        placed_bombs = 0
        while placed_bombs < num_bombs:
            x, y = random.randint(0, self.gridSize - 1), random.randint(0, self.gridSize - 1)
            if self.bombMap[x][y] == 0:
                self.bombMap[x][y] = 1
                placed_bombs += 1

    def calculate_numbers(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                if self.bombMap[x][y] == 1:
                    continue
                count = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.gridSize and 0 <= ny < self.gridSize and self.bombMap[nx][ny] == 1:
                        count += 1
                self.numMap[x][y] = count
    
    

Minesweeper()