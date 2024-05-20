import tkinter as tk
import random

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('2048')
        self.window.geometry('400x430')

        self.canvas = tk.Canvas(self.window, bg='white', width=400, height=400)
        self.canvas.pack()

        self.new_game_button = tk.Button(self.window, text='New Game', command=self.new_game)
        self.new_game_button.pack()

        self.grid = [[0]*4 for _ in range(4)]
        self.score = 0

        self.draw_grid()
        self.place_new_tile()
        self.place_new_tile()

        self.window.bind('<Key>', self.move)

    def draw_grid(self):
        for i in range(4):
            for j in range(4):
                self.canvas.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill='light gray', outline='gray')
                self.canvas.create_text(j*100+50, i*100+50, text=str(self.grid[i][j]), font=('Arial', 24, 'bold'))

    def place_new_tile(self):
        available_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if available_cells:
            i, j = random.choice(available_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
            self.update_grid()

    def move(self, event):
        if event.keysym in ('Up', 'Down', 'Left', 'Right'):
            if event.keysym == 'Up':
                self.shift_tiles(-1, 0)
            elif event.keysym == 'Down':
                self.shift_tiles(1, 0)
            elif event.keysym == 'Left':
                self.shift_tiles(0, -1)
            elif event.keysym == 'Right':
                self.shift_tiles(0, 1)
            self.place_new_tile()

    def shift_tiles(self, dx, dy):
        moved = False
        for i in range(4):
            for j in range(4):
                x, y = i+dx, j+dy
                while 0 <= x < 4 and 0 <= y < 4:
                    if self.grid[x][y] == 0:
                        self.grid[x][y] = self.grid[i][j]
                        self.grid[i][j] = 0
                        i, j = x, y
                        x, y = i+dx, j+dy
                        moved = True
                    elif self.grid[x][y] == self.grid[i][j]:
                        self.grid[x][y] *= 2
                        self.grid[i][j] = 0
                        self.score += self.grid[x][y]
                        moved = True
                        break
                    else:
                        break
                    x, y = x+dx, y+dy
        if moved:
            self.update_grid()

    def update_grid(self):
        self.canvas.delete('all')
        self.draw_grid()
        self.window.update()

    def new_game(self):
        self.grid = [[0]*4 for _ in range(4)]
        self.score = 0
        self.canvas.delete('all')
        self.draw_grid()
        self.place_new_tile()
        self.place_new_tile()

if __name__ == "__main__":
    game = Game2048()
    game.window.mainloop()