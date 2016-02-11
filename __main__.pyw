"""
__main__.pyw is a part of Snake-Game.
Copyright (C) 2016  Shubham Mishra

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from Tkinter import *
from random import randrange 
import os, sys

class Food(Label):
    def __init__(self, root, **kwargs):
        self.image = PhotoImage(file='Snake-Game\Food.gif').subsample(12, 12)
        Label.__init__(self, root, image=self.image, bd=0)
        self.root = root 
        
        self.x = 0
        self.y = 0 
        
        self.reset() 
        
    def reset(self):
        self.x = randrange(0, 95, 5)
        self.y = randrange(0, 95, 5) 
        
        self.place(relx=(self.x / 100.0), rely=(self.y / 100.0)) 
        
class Snake(Label):
    def __init__(self, root, **kwargs):
        self.images = [PhotoImage(file='Snake-Game\Head.gif').subsample(8,8), 
                       PhotoImage(file='Snake-Game\Body.gif').subsample(8, 8)]

                       
        Label.__init__(self, root, image=self.images[0], bd=0)
        self.root = root 
        
        self.moveVector = 'Right' #Can also be 'Left', 'Up', 'Down', 'p'(ause)
        self.x = 45 
        self.y = 45 
        
        self.body = []
        self.addBody()
        
        self.points = 0 
        
        self.root.after(500, self.move)
        
    def move(self):
        buffx = self.x 
        buffy = self.y 
        
        #Head movement
        if self.moveVector == 'Right':
            self.x += 5 
        elif self.moveVector == 'Left':
            self.x -= 5 
        elif self.moveVector == 'Up':
            self.y -= 5 
        elif self.moveVector == 'Down':
            self.y += 5 
            
        self.place(relx=(self.x / 100.0), rely=(self.y / 100.0)) 
        
        #Body movement 
        for part in self.body:
            x = part.winfo_x() / float(self.root.winfo_width()) * 100
            y = part.winfo_y() / float(self.root.winfo_height()) * 100
            
            buffx, buffy, x, y = x, y, buffx, buffy 
            
            part.place(relx=(x / 100.0), rely=(y / 100.0))
            
        #Wall bump 
        if self.x in (-5, 105) or self.y in (-5, 105):
            startover()
        
        eat() #Checks if it has eaten or not     
        
        #Speed increases with points 
        if self.points < 480:
            self.root.after((500 - self.points), self.move)
        else:
            self.root.after(10, self.move)
            
    def changeDirection(self, event):
        key = event.keysym 
        
        if key in ['Up', 'Down', 'Left', 'Right', 'p']:
            self.moveVector = key 
            
    def addBody(self):
        tail = Label(self.root, image=self.images[1], bd=0)
        tail.place(relx=(self.x / 100.0), rely=(self.y / 100.0))
        self.body.append(tail) 
        
def eat():
    if snake.x == food.x and snake.y == food.y:
        snake.points += 10
        root.title('Snake Game | Points: %s' % snake.points)
        food.reset()
        snake.addBody()
        
def startover(): 
    os.execl(sys.executable, sys.executable, *sys.argv)
    
root = Tk()
root.title('Snake Game')
root.config(bg='cyan')

food = Food(root)
snake = Snake(root)
 
root.bind("<Key>", snake.changeDirection)

root.geometry('600x500')
root.resizable(height=False, width=False)
root.mainloop()            
            
            
            
        
        
        