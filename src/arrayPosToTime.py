#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# arrayPosToTime.py

# Reverse of timeToArrayPos - take an array position and turn it into a time

def arrayDay(day):
    days = {0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday"
            }

    day = days.get(day, "No timeslot available.")
    print(day, end=" ")
    return day

def arrayTime(time):
    if (time == -1):
        print("Gonna have to work a weekend.", end="")
        return
    
    hour = int(time / 12) + 8
    if (hour == 12):
        pm = True
    elif (hour > 12):
        hour -= 12
        pm = True
    else:
        pm = False

    minutes = (time % 12) * 5

    print(hour, end="")
    print(":", end="")
    if (minutes < 10):
        print("0", end="")
    print(minutes, end="")
    print("PM" if pm == True else "AM", end="")
    return [hour, minutes, pm]
