"""
This program is to scrap the real-time stock price from Yahoo Finance.
Programmer: Phuong V. Nguyen
Email: phuong.nguyen@economics.uni-kiel.de
"""

get_ipython().run_line_magic('matplotlib', 'notebook')

from yahoo_fin import stock_info as si
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from threading import Thread
import time
stock_name='aapl'
class LiveGraph:
    def __init__(self):
        self.x_data, self.y_data = [], []
        self.figure = plt.figure(figsize=(7,5))
        self.line, = plt.plot(self.x_data, self.y_data,color='b',linewidth=3)
        plt.suptitle('The Real-Time Price of The Stock '+ stock_name)
        plt.grid(color='r', linestyle='--', linewidth=0.5)
        plt.grid(True)
        #plt.tight_layout
        self.animation = FuncAnimation(self.figure, self.update, interval=1000)
        self.th = Thread(target=self.thread_f, daemon=True)
        self.th.start()

    def update(self, frame):
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        return self.line,

    def show(self):
        plt.show()

    def thread_f(self):
        x = 0
        while True:
            self.x_data.append(x)
            x += 1
            self.y_data.append(si.get_live_price(stock_name))   #randrange(0, 100)
            time.sleep(1)  

g = LiveGraph()
g.show()