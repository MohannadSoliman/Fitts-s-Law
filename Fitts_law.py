from tkinter import *
import random
import numpy as np
import matplotlib.pyplot as plt
import time
root = Tk()

time1 = 0
time2 = 0
isStart = True

IDs = []
times = []


def calculate_ID(width, distance):
    initial_distance = 10  #distance between button1 and button2 in grid(initialization)
    distance += initial_distance
    ID = np.log2(2*distance/width)
    return ID



def clicking1(widget1, widget2):
    global time1
    global isStart
    time1 = time.time()
    if not isStart:
        times.append(1000*(time1 - time2))
    random_distance = random.randint(0, 600)
    random_width = random.randint(7, 75)
    IDs.append(calculate_ID(random_width, random_distance))
    widget2.config(width = random_width)
    widget1.config(width = random_width)
    isStart = False

def clicking2(widget1, widget2):
    global time2
    time2 = time.time()
    random_distance = random.randint(0, 600)
    random_width = random.randint(7, 75)
    IDs.append(calculate_ID(random_width, random_distance))
    times.append(1000*(time2 - time1))
    widget2.config(width = random_width)
    widget2.grid(row=5, column=9, pady=200, padx=random_distance)
    widget1.config(width = random_width)


def drawing():
    plt.ylim(0, 1200)
    plt.xlim(0, 8)
    plt.ylabel("Time (ms)")
    plt.xlabel("Index of difficulty")
    x = np.array(IDs[0:len(IDs)-1])
    y = np.array(times)
    plt.plot(x, y, 'o')
    b, a = np.polyfit(x, y, 1)
    plt.plot(x, a + b*x, c='black')
    plt.text(1, 1170,'a = ' + str(a) + 'ms')
    plt.text(1, 1100, 'b = ' + str(b))
    plt.grid()
    plt.show()

def main():
    button1 = Button(root, text="Button 1", padx=0, pady=250, bg = 'red')
    button2 = Button(root, text="Button 2", padx=0, pady=250, bg = 'red')
    button3 = Button(root, text="Show graph", command=drawing)
    button1['command'] = lambda w1=button1, w2=button2: clicking1(w1, w2)
    button2['command'] = lambda w1=button1, w2=button2: clicking2(w1, w2)
    button1.grid(row=5, column=1, pady=200, padx=10)
    button2.grid(row=5, column=9, pady=200, padx=0)
    button3.grid(row=0, column=0, padx=10)
    root.mainloop()

main()