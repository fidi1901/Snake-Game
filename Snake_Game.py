#==========================================
# Purpose:
# - Represents the tk board, boundaries, player snakes, enemy snakes and pellets that will be animated
# Instance variables:
# self.win - creates a tkinter window
# self.canvas - represents the size of the tkinter window
# self.board - represents the boundaries that the snake game is to be played within
# self.x - the upper left hand x coordinate of the pellet
# self.y - the upper left hand y coordinate of the pellet
# self.snake - the player snake, which is an object of class Snake
# self.enemy - the enemy snake, which is an object of class Enemy
# self.pellet - represents the food pellet
# Methods:
# __init__ - the constructor method that defines the instance variables
# reset - the reset method which allows the game to restart once the game is over
# gameloop - the method which allows the player snake, enemy snake, and pellet to animate
# and defines how the snakes and pellet animate depending on their position
#==========================================
import tkinter as tk
import random
class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, width=660, height=660)
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.x = random.randint(1, 20) * 30
        self.y = random.randint(1, 20) * 30
        self.snake = Snake(330, 330, 'green', self.canvas)
        self.enemy = Enemy(210, 210, 'red', self.canvas)
        self.pellet = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill='brown')
        self.canvas.pack()
        self.win.bind('<Down>',self.snake.go_down)
        self.win.bind('<Up>',self.snake.go_up)
        self.win.bind('<Left>',self.snake.go_left)
        self.win.bind('<Right>',self.snake.go_right)
        self.win.bind('r',self.reset)
        self.gameover = False
        self.gameloop()
    def reset(self, event):
        self.canvas.delete(tk.ALL)
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.x = random.randint(1, 20) * 30
        self.y = random.randint(1, 20) * 30
        self.snake = Snake(330, 330, 'green', self.canvas)
        self.enemy = Enemy(210, 210, 'red', self.canvas)
        self.pellet = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill='brown')
        self.canvas.pack()
        self.win.bind('<Down>',self.snake.go_down)
        self.win.bind('<Up>',self.snake.go_up)
        self.win.bind('<Left>',self.snake.go_left)
        self.win.bind('<Right>',self.snake.go_right)
        self.win.bind('r',self.reset)
        self.gameover = False
        self.gameloop()
    def gameloop(self):
        if self.gameover == False:
            var2 = self.enemy.enemy_move(self.pellet)
            var = self.snake.move(self.pellet)
            var1 = self.snake.itself()
            var3 = self.enemy.hit(self.snake)
            var4 = self.enemy.itself()
            if var == 3 or var2 == 3:
                self.canvas.delete(self.pellet)
                self.px = random.randint(1, 20) * 30
                self.py = random.randint(1, 20) * 30
                self.pellet = self.canvas.create_oval(self.px, self.py, self.px + 30, self.py + 30, fill='brown')
            if var1 == True or var == True or var3 == True:
                self.text = self.canvas.create_text(200,200,text='Game Over! Score: ' + str(len(self.snake.segments)))
                self.gameover = True
            if var4 == 3:
                self.canvas.delete(self.enemy)
            self.canvas.after(100, self.gameloop)





#==========================================
# Purpose:
# Defines the characteristics of the player snake; it's upper left hand x and y coordiantes, the color
# of the snake, and the tKinter window that snake will be placed upon
# Instance variables:
# self.x - the upper left hand x coordinate of the snake
# self.y - the upper left hand y coordinate of the snake
# self.color - the color of the snake
# self.canvas - represents the tKinter window the snake will play on
# self.cr - the first segment of the snake, which first appears when the game starts
# self.segments - a list containing the coordinates body of each segment of the snake
# self.vx - the velocity of the self.x coordinate
# self.vy - the velocity of the self.y coordinate
# Methods:
# __init__ - the constructor method used to define the instance variables
# move - the method used to determine how the snake moves
# itself - the method that explains how the snake would touch itself
# go_down - the method that changes the velocity of the x and y coordinates to make the snake go down
# go_up - same as go_down, but changes the velocity, to make it go right
# go_right - changes the velocity to make the snake go right
# go_left - changes the velocity to make the snake go left
#==========================================
class Snake:
    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.segments = []
        self.cr = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill=self.color)
        self.segments.append(self.cr)
        self.vx = 30
        self.vy = 0
    def move(self, pellet):
        self.x += self.vx
        self.y += self.vy
        if self.x < 30 or self.x >= 630:
            return True
        elif self.y < 30 or self.y >= 630:
            return True
        self.cr2 = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill=self.color)
        self.segments.insert(0,self.cr2)
        if self.canvas.coords(self.segments[0]) != self.canvas.coords(pellet):
            var = self.segments.pop(-1)
            self.canvas.delete(var)
            return 2
        else:
            return 3


    def itself(self):
        for i in self.segments[1:]:
            if self.canvas.coords(self.segments[0]) == self.canvas.coords(i):
                return True
        return False
    def go_down(self,event):
        self.vx = 0
        self.vy = 30
    def go_up(self,event):
        self.vx = 0
        self.vy = -30
    def go_left(self,event):
        self.vx = -30
        self.vy = 0
    def go_right(self,event):
        self.vx = 30
        self.vy = 0

#==========================================
# Purpose:
# Represents the characteristics of the enemy snake, which is derived from the Snake class
# Instance variables:
# Instance variables in Enemy class are inherited from the Snake class
# Methods:
# __init__ - the constructor method which is inherited by the constructor method from the Snake class
# go_down, go_up, go_left, and go_right are exact same methods as the said methods from the Snake class
# enemy_move - the method that explains how the enemy moves in certain situations
# hit - the method that explains how the player snake and enemy snake would hit each other
#==========================================
class Enemy(Snake):
    def __init__(self, x, y, color, canvas):
        Snake.__init__(self, x, y, color, canvas)
    def go_down(self):
        self.vx = 0
        self.vy = 30
    def go_up(self):
        self.vx = 0
        self.vy = -30
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def go_right(self):
        self.vx = 30
        self.vy = 0

    def enemy_move(self, pellet):
        lst = self.canvas.coords(pellet)
        if lst[0] > self.x:
            self.go_right()
        elif lst[0] < self.x:
            self.go_left()
        elif lst[1] < self.y:
            self.go_up()
        elif lst[1] > self.y:
            self.go_down()
        self.x += self.vx
        self.y += self.vy
        self.cr2 = self.canvas.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill=self.color)
        self.segments.insert(0,self.cr2)
        if self.canvas.coords(self.segments[0]) != self.canvas.coords(pellet):
            var = self.segments.pop(-1)
            self.canvas.delete(var)
            return 2
        else:
            return 3

    def hit(self, snake):
        for i in self.segments:
            for j in snake.segments:
                if self.canvas.coords(j) == self.canvas.coords(i):
                    return True
SnakeGUI()
tk.mainloop()
