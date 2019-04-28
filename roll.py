import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
clk=20
dt=16
sw=9
rollcount=0
lastb=0
currentb=0
def clkdown(pin):
    global rollcount,lastb,currentb
    lastb=gpio.input(dt)
    while not gpio.input(clk):
        pass
    currentb=gpio.input(dt)
    if (lastb==1) and (currentb==0):
        print("shun")
        rollcount+=1
        print(rollcount)
    if (lastb==0) and (currentb==1):
        print("ni")
        rollcount-=1
        print(rollcount)
def swdown(pin):
    global rollcount
    rollcount=0
    print("clear:0")
def init():
    global clk,dt,sw
    gpio.setup(clk,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.setup(dt,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.setup(sw,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(clk,gpio.FALLING,callback=clkdown)
    #gpio.add_event_detect(dt,gpio.BOTH,callback=dtdown)
    gpio.add_event_detect(sw,gpio.FALLING,callback=swdown)
if __name__=="__main__":
    init()
        

    