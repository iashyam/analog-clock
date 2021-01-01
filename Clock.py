from tkinter import *
from PIL import Image, ImageTk
import time
import math

class clock:
    def __init__(self):
        self.window= Tk()
        self.window.title('Clock')
        self.lc = math.pi/30
        self.lc_hr = math.pi/6
        self.lc_hrm = math.pi/(6*60)
        self.text = "Happy NEw YEar"

        self.img = ImageTk.PhotoImage(Image.open('clock.png'))

        self.show_time()
        self.move()

        self.window.mainloop()

    def move(self):
        while True:
            self.window.after(100)
            self.show_time2()
            self.window.update()

    def show_time(self):
        self.canvas = Canvas(self.window, height=500, width=500,bd=2)
        self.canvas.pack()
        self.canvas.create_image(250,250, image=self.img)
        self.canvas.create_oval(246, 246, 254, 254, fill='black',tags='circle', width=2)
        self.canvas.create_line(self.polar(100, self.lc * self.second()) ,tags='second',fill='green')
        self.canvas.create_line(self.polar(70, (self.lc_hr * self.hour()+self.lc_hrm*self.miniute())), width=4,arrow=LAST, tags = 'Hour')
        self.canvas.create_line(self.polar(95, self.lc * self.miniute()), width=2,arrow=LAST, tags='minute')
        self.canvas.create_text(250, 90,text=self.text, font='times 20 bold')
    
    def show_time2(self):
        self.canvas.destroy()
        self.show_time()
        self.text=time.strftime('%H:%M:%S')
        
    def polar(self, radius, theta):
        return 250, 250, (250 + radius* math.sin(theta)), (250- radius*math.cos(theta))

    def hour(self):
        hr = int(time.strftime('%H'))
        if hr>=12:
            return hr-12
        else:
            return hr

    def miniute(self):
        return int(time.strftime('%M'))

    def second(self):
        return int(time.strftime('%S'))

if __name__ == '__main__':
    try:
        clock()
    except:
        pass
