from tkinter import *
import random
WIDTH = 500
HEIGHT = 500
Snake_size = 15
root = Tk()
c = Canvas(root , width =WIDTH, height= HEIGHT,background="black")
c.pack()
Snake = c.create_rectangle(WIDTH/2-Snake_size,HEIGHT/2-Snake_size,WIDTH/2+Snake_size,HEIGHT/2+Snake_size,fill="yellow")
Snake_speed_x = 1
Snake_speed_y = 1
Snakes_speed = 10
class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                         x+Snake_size, y+Snake_size,
                         fill="white")
class Sneak(object):
    def __init__ (self,segments):
        self.segments = segments
    def move_snake(self):
        SNAKES = {Snake: Snake_speed_x,Snake: Snake_speed_y}
        for snake in SNAKES:
            x= Snake_speed_x
            y=Snake_speed_y
            c.move(Snake,x,y)
        if c.coords(snake)[1] <0:
            c.move(snake,0,-c.coords(snake)[1])
        elif c.coords(snake)[3] > HEIGHT:
            c.move(Snake,0,HEIGHT - c.coords(snake)[3])
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            # задаем каждому сегменту позицию сегмента стоящего после него
            c.coords(segment, x1, y1, x2, y2)
    c.focus_set()



    def movement_handler(self,event):
        global Snake_speed_x,Snake_speed_y
        if event.keysym == "w":
            Snake_speed_y = -Snakes_speed
        elif event.keysym == "s":
            Snake_speed_y = Snakes_speed
        elif event.keysym == "a":
            Snake_speed_x = -Snakes_speed
        elif event.keysym == "d":
            Snake_speed_x = Snakes_speed
    c.bind("<KeyPress>", movement_handler)
    def stop_snake(event):
        global Snakes_speed,Snake_speed_y,Snake_speed_x
        if event.keysym in "a":
            Snake_speed_y = 0
        elif event.keysym in "w":
            Snake_speed_x = 0
        elif event.keysym in "s":
            Snake_speed_x = 0
        elif event.keysym in "d":
            Snake_speed_y = 0
    c.bind("<KeyRelease>", stop_snake)
def main():
    Snake.move_snake()
    root.after(30, main)
main()
Snake.food()
root.mainloop()