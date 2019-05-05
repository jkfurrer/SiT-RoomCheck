#!/usr/bin/env python3

# James K. Furrer
# Electrical Engineering
# Stevens Institute of Technology '19
# E: jkfurrer@gmail.com

# availability

# Given a time and room schedule, provide a function to determine the next availble timeslot for a specififed amount of time

def freeTime(currentTime, roomSched, slotLength=10):
    day = currentTime.getDayIndex()
    time = currentTime.getTimeIndex()
    slotLength = int(slotLength / 5)
    if (time + slotLength > 144):
        if (day >= 4):
            day = 0
            time = 0
        else:
            day += 1
            time = 0
        print("Not enough time left today!")
        
    # Check the rest of current day first and foremost
    for x in range(time, 144):
        if (roomSched[day][x] == True):
            for t in range(slotLength):
                if (roomSched[day][x+t] == True):
                    flag = True
                else:
                    flag = False
                    x += t
                    break
            if (flag == True):
                return [day, x, x+slotLength]
        else:
            continue

    # If there was no return in the above loop, a timeslot was not found for the rest of that day.
    # From here on, examine the rest of the entire days

    origDay = day
    day +=1
    
    for y in range (day, 5):
        for x in range(0, 144):
            if (roomSched[y][x] == True):
                for t in range(slotLength):
                    if (roomSched[y][x+t] == True):
                        flag = True
                    else:
                        flag = False
                        x += t
                        break
                if (flag == True):
                    return [y, x, x+slotLength]
            else:
                continue

    # If it's still not found, wrap around to the beginning of the week again
    day = 0
    
    for y in range (day, origDay):
        for x in range(0, 144):
            if (roomSched[y][x] == True):
                for t in range(slotLength):
                    if (roomSched[y][x+t] == True):
                        flag = True
                    else:
                        flag = False
                        x += t
                        break
                if (flag == True):
                    return [y, x, x+slotLength]
            else:
                continue

    # If it's still not found, try times before the starting time of the original day (EG, you just missed it)
    day = origDay
    
    for x in range(0, time):
        if (roomSched[day][x] == True):
            for t in range(slotLength):
                if (roomSched[day][x+t] == True):
                    flag = True
                else:
                    flag = False
                    x += t
                    break
            if (flag == True):
                return [day, x, x+slotLength]
        else:
            continue

    # Still not found? Well, then I guess there are no time slots available. Looks like somebody's gonna have to work the weekend.

    return [-1, -1, -1]
