from tkinter import *
import time
from PIL import ImageTk,Image
from math import sin, cos, pi

class Clock:
    def __init__(self):

        #defining the constants
        self.WIDTH = 500
        self.HEIGHT = 500
        self.center  = (self.HEIGHT/2, self.WIDTH/2)
        self.RADIUS = self.WIDTH/2

        self.lc_hr = pi/6 #deffing the least counts
        self.lc_min = pi/30
        self.hc = self.lc_hr/60

        self.window = Tk()
        self.window.title("Clock")
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        #creatinga a sheet for clock
        self.canvas = Canvas(self.window, width = self.WIDTH, height =self.HEIGHT)
        img = ImageTk.PhotoImage(Image.open("clock.png"))
        self.canvas.create_image(self.center[0], self.center[1], image=img)
        self.canvas.pack()
        self.drawHands()

        while True:
            self.canvas.after(200, self.move)
            self.canvas.update()
            
        self.window.mainloop()


    def drawHands(self):
        hr, mn, sec = self.getTime()
        self.canvas.create_line(self.polar(0,0), self.polar(self.RADIUS/4, self.lc_hr*hr+self.hc*mn), width = 4, tags='hour', fill='green')
        self.canvas.create_line(self.polar(0,0), self.polar(self.RADIUS//3, self.lc_min*mn), width = 1.5, tags='min', fill='blue')
        self.canvas.create_line(self.polar(0,0), self.polar(self.RADIUS//2.5, self.lc_min*sec),tags='sec', fill='red')

    def move(self):
        self.canvas.delete('hour', 'min', 'sec')
        self.drawHands()

    def getTime(self):
        hr = int(time.strftime('%H'))
        mn = int(time.strftime('%M'))
        sec = int(time.strftime('%S'))
        return hr, mn, sec
        
    def polar(self,r, theta):
        centerX, centerY = self.center
        x = centerX + r*sin(theta)
        y = centerY - r*cos(theta)
        return x, y

if __name__ == '__main__':
    try:
        Clock()
    except:
        pass
