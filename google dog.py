from tkinter import *
import time
import random

class Sprite:
    def __init__(self, canvas):
        self.pos = None
        self.canvas = canvas
        self.sprite = None
        self.vx = 0
        self.vy = 0

    def update(self):
        if self.canvas is not None and self.sprite is not None:
            self.canvas.move(self.sprite, self.vx, self.vy)
            self.pos = self.canvas.coords(self.sprite)
        return self

    def create(self, coords):
        self.sprite = self.canvas.create_polygon(coords)
        self.pos = self.canvas.coords(self.sprite)

    def destroy(self):
        self.sprite.remove()

    def alive(self):
        return True

        
class Square(Sprite):
    def __init__(self, canvas):
        super().__init__(canvas)

    def makeCoords(self, x1,y1,l):
        return (x1,y1, x1+l,y1, x1+l,y1+l, x1,y1+l)

    def create(self, x1, y1):
        super().create(self.makeCoords(x1, y1, 30))

    def left(self):
        return self.pos[0]

    def bottom(self):
        return self.pos[1]

    def top(self):
        return self.pos[5]

    def right(self):
        return self.pos[4]

    def collision(self, square):
        return ((self.pos[4] >= square.pos[0] and self.pos[4] <= square.pos[2])
            and (self.pos[5] >= square.pos[1] or self.pos[7] >= square.pos[3]))


class ObstacleSquare(Square):
    def __init__(self, canvas):
        print('ObstacleSquare Created')
        super().__init__(canvas)
        self.vx = -3
        self.create(505,150)
        random_color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
        self.canvas.itemconfig(self.sprite, fill=random_color)

    def alive(self):
        if self.right() > 0:
            return True
        else:
            self.canvas.delete(self.sprite)
            return False


class PlayerSquare(Square):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.floor = 150
        self.ceil = 75
        self.create(50,150)
        self.canvas.bind_all('<space>', self.jump)
 
    def jump(self, event):
        print('jump')
        if self.bottom() >= self.floor:
            self.vy = -4
            
    def update(self):
        if self.top() <= self.ceil and self.vy == -4:
            self.vy = 4
        if self.bottom() >= self.floor and self.vy == 4:
            self.vy = 0
        super().update()
        
    def alive(self, sprites):
        return len([s for s in sprites if self.collision(s)]) == 0


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("InfiRun")
        self.tk.resizable(0, 0)
        self.canvas = Canvas(self.tk, width=500, height=250)
        self.canvas.pack()
        self.player = PlayerSquare(self.canvas)
        self.boxes = None
        self.canvas.bind_all('<Return>', self.reset)
        self.splash = self.canvas.create_text(250, 130, text='press <enter> to begin', fill='black', font=('Helvetica', 20))
        self.mainloop()
    
    def reset(self, event):
        if self.boxes is not None:
            [self.canvas.delete(b.sprite) for b in self.boxes] 
        self.boxes = [ObstacleSquare(self.canvas)]
        self.canvas.itemconfig(self.splash, text='')
        
    def mainloop(self):
        while True:
            #rest
            while self.boxes is None:
                self.tk.update()
                time.sleep(.01)
            #play
            while self.player.alive(self.boxes):
                if ((random.randint(0, 100) > 99 and self.boxes[-1].right() <= 400)
                    or (len(self.boxes) == 1 and self.boxes[0].left() < 150)):
                    self.boxes.append(ObstacleSquare(self.canvas))
                    print(len(self.boxes))
                
                self.tk.update()
                
                self.boxes = [b.update() for b in self.boxes if b.alive()]
                self.player.update()
                time.sleep(0.01)
            #reset
            [self.canvas.delete(b.sprite) for b in self.boxes]
            self.boxes = None
            self.canvas.itemconfig(self.splash, text='GAME OVER\npress <enter> to begin')
        

if __name__ == '__main__':
    Game()