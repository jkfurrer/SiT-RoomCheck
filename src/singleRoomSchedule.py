#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology
# E: jkfurrer@gmail.com

#singleRoomSchedule

# Takes two arguements: what is the current semester, and what room are we interested in?

# The starting and end times for some classes are pretty weird, but usually are no more specific than increments of 5 minutes. The earliest class starts at 8am, and IT is only open until 8pm. To make an array of time slots to indicate whether a class was in session or not would need 144 elements per day of the week. There are some saturday classes on the schedule, however these will be ignored since IT does not work on the weekends. This is a total of 720 elements needed to be processed. This array alone would be 720 bytes at a minimum. This can be simplified significantly using

import timeToArrayPosition

def singleRoomSchedule(semester, room):
    timeTable = [[True for y in range(144)] for x in range(5)]
    
    days = {"M":0,
            "T":1,
            "W":2,
            "R":3,
            "F":4
            }

    daysRev = {0:"M",
            1:"T",
            2:"W",
            3:"R",
            4:"F"
            }
    
    with open("../resources/" + semester + ".txt", "r") as schedule:
        for line in schedule:
            if (line.strip() != ""):
                currentLineRoom = line.strip().split(",")[6].strip()
                currentLineRoom += line.strip().split(",")[7].strip()
                if (currentLineRoom == room):
                    dayOfWeek = line.strip().split(",")[2].strip().upper()
                    if (dayOfWeek == "TBA" or dayOfWeek == "TBD"):
                        continue
                    #print(dayOfWeek)
                    startTime = line.strip().split(",")[3].strip().upper()
                    #print(startTime)
                    endTime = line.strip().split(",")[4].strip().upper()
                    #print(endTime)

                    dayOfWeek = list(dayOfWeek)
                    for day in dayOfWeek:
                        dayIndex = days.get(day, -1)
                        if dayIndex == -1:
                            # For some reason the day of the week is not M-F. There are some saturday classes: ignore these
                            continue
                    
                        startTimeIndex = timeToArrayPosition.pos(startTime)
                        endTimeIndex = timeToArrayPosition.pos(endTime)

                        for index in range(startTimeIndex, endTimeIndex):
                            timeTable[dayIndex][index] = False
    schedule.close()

    #Print out a table visually for inspection and debugging
    
    print(" |    8AM     ", end="")
    print("|    9AM     ", end="")
    print("|    10AM    ", end="")
    print("|    11AM    ", end="")
    print("|    12PM    ", end="")
    print("|    1PM     ", end="")
    print("|    2PM     ", end="")
    print("|    3PM     ", end="")
    print("|    4PM     ", end="")
    print("|    5PM     ", end="")
    print("|    6PM     ", end="")
    print("|    7PM     |")
    
    for y in range(0,5):
        print(daysRev.get(y, "X"), end="")
        for x in range(0,144):
            if (x % 12 == 0):
                print("|", end="")
            print("X" if timeTable[y][x] == False else "_", end="")
        print("|")
    print()
    return timeTable
