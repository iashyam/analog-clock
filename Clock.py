from tkinter import *
import time
import math

class clock:
    def __init__(self):
        self.window= Tk()
        self.window.title('Clock')
        self.lc = math.pi/30
        self.lc_hr = math.pi/6

        self.show_time()
        self.move()

        self.window.mainloop()

    def move(self):
        while True:
            self.window.after(100)
            self.show_time2()
            self.window.update()

    def show_time(self):
        self.canvas = Canvas(self.window, height=500, width=500)
        self.canvas.pack()
        self.canvas.create_oval(60, 60, 440, 440, tags='circle', width=2)
        self.canvas.create_line(self.polar(180, self.lc * self.second()) ,tags='second')
        self.canvas.create_line(self.polar(150, self.lc_hr * self.hour()), width=4,arrow=LAST, tags = 'Hour')
        self.canvas.create_line(self.polar(175, self.lc * self.miniute()), width=2,arrow=LAST, tags='minute')
        for i in range(12):
            if i%3 == 0:
                self.canvas.create_line(self.polar3((self.lc_hr)*i) , width=4)
            else:
                self.canvas.create_line(self.polar3((self.lc_hr) * i))

    def show_time2(self):
        self.canvas.destroy()
        self.show_time()

    def polar(self, radius, theta):
        return 250, 250, (250 + radius* math.sin(theta)), (250- radius*math.cos(theta))

    def polar3(self, theta):
        return (250 + 180* math.sin(theta)), (250- 180*math.cos(theta)), (250 + 190* math.sin(theta)), (250- 190*math.cos(theta))

    def hour(self):
        hr = int(time.strftime('%H'))
        if hr>=12:
            return hr-12
        else:
            return hr

    def miniute(self):
        m = int(time.strftime('%M'))
        return m

    def second(self):
        return int(time.strftime('%S'))

    def refresh(self):
        clock()




if __name__ == '__main__':
    try:
        clock()
    except:
        pass