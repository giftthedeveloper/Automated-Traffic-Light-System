#   Hi i'm Gift Jeremiah. I'm a python developer and an upcoming AI ENGR(IN VIEW)
#SPECIAL THANKS TO GOD FOR MAKING THIS PROJECT A SUCESS.
#You can reach out to me via my mail giftjeremiah001



# A ROUND ABOUT traffic light system.

from machine import Pin
import utime

#red1 refers to the red LIGHT of lane 1
#red1_opp refers to the RED LIGHT OF the opposite lane of the road.

#DEFINING VARIABLES FOR THE TRAFFIC LIGHT SYSTEM
red1 = Pin(,Pin.OUT)
red1_opp= Pin(,Pin.OUT)
red2 = Pin(,Pin.OUT)
red2_opp = Pin(, Pin.OUT)


green1 = Pin(,Pin.OUT)
green1_opp= Pin(,Pin.OUT)
green2 = Pin(,Pin.OUT)
green2_opp = Pin(, Pin.OUT)

yellow1 = Pin(,Pin.OUT)
yellow1_opp= Pin(,Pin.OUT)
yellow2 = Pin(,Pin.OUT)
yellow2_opp = Pin(, Pin.OUT)


def start():
    red1.high()
    red1_opp.high()
    red2.high()
    red2_opp.high()
    yellow1.high()
    yellow1_opp.high()
    yellow2.low()
    yellow2_opp.low()
    utime.sleep(2)

def phase2():
    red1.low()
    yellow1.high()
    red1_opp.low()
    yellow1_opp.high()
    red2.high()
    red2_opp.high()
    utime.sleep(5)

def phase3():
    yellow1.low()
    green1.high()
    yellow1_opp.low()
    green1_opp.high()
    red2.high()
    red2_opp.high()
    utime.sleep(12)

def phase4():
    green1.low()
    red1.high()
    red1_opp.high()
    yellow2.high()
    yellow2_opp.high()
    green1_opp.low()
    utime.sleep(4)

def phase5():
    red1.high()
    red1_opp.high()
    yellow2_opp.low()
    yellow2.low()
    green2.high()
    green2_opp.high()
    red2.low()
    red2_opp.low()
    utime.sleep(12)

def phase6():
    green2.low()
    green2_opp.low()
    red2.high()
    red2_opp.high()
    utime.sleep(2)

while True:
    start()
    phase2()
    phase3()
    phase4()
    phase5()
    phase6()



